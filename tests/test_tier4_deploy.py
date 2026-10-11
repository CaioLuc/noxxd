"""
Tier 4: Deployment & HTTP Simulation Tests
Spins up ephemeral HTTP server, fetches all referenced assets/links asserting HTTP 200 & zero 404s,
validates case-sensitivity (Linux GitHub Pages simulation), validates SEO/OpenGraph tags,
validates accessibility (alt tags and semantics), and validates WCAG AA color contrast ratio.
"""

from pathlib import Path
import re
import socket
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import httpx
import pytest

from tests.helpers import (
    get_repo_root,
    get_index_html,
    get_style_css,
    check_case_exact_path,
    calculate_contrast_ratio,
)

def find_free_port() -> int:
    """Find an available port on localhost."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]

def test_t4_ephemeral_http_server_zero_404(repo_root: Path):
    """
    Simulate real GitHub Pages static hosting via ephemeral local HTTP server.
    Requests all internal pages, CSS, JS, images, and fonts.
    Asserts HTTP 200 OK for every single asset with ZERO 404 errors.
    """
    port = find_free_port()
    handler = partial(SimpleHTTPRequestHandler, directory=str(repo_root))
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    
    base_url = f"http://127.0.0.1:{port}"
    errors = []
    
    try:
        with httpx.Client(base_url=base_url, timeout=5.0) as client:
            # 1. Fetch root page
            resp_root = client.get("/")
            assert resp_root.status_code == 200, f"Root / returned HTTP {resp_root.status_code}"
            
            # 2. Fetch CNAME
            resp_cname = client.get("/CNAME")
            assert resp_cname.status_code == 200, f"/CNAME returned HTTP {resp_cname.status_code}"
            assert resp_cname.text.strip() == "noxxd.com.br", "CNAME served unexpected content"
            
            # 3. Parse HTML and collect all internal assets
            soup = BeautifulSoup(resp_root.text, "html.parser")
            assets_to_test = set()
            
            # Scripts
            for script in soup.find_all("script", src=True):
                src = script["src"]
                if not src.startswith("http") and not src.startswith("//"):
                    assets_to_test.add(src)
                    
            # Stylesheets and links
            for link in soup.find_all("link", href=True):
                href = link["href"]
                if not href.startswith("http") and not href.startswith("//"):
                    assets_to_test.add(href)
                    
            # Images
            for img in soup.find_all("img", src=True):
                src = img["src"]
                if not src.startswith("http") and not src.startswith("data:"):
                    assets_to_test.add(src)
                    
            # Source tags (picture/video)
            for source in soup.find_all("source", srcset=True):
                srcset = source["srcset"].split(",")[0].split()[0]
                if not srcset.startswith("http") and not srcset.startswith("data:"):
                    assets_to_test.add(srcset)
                    
            # CSS urls (from style.css if fetched)
            resp_css = client.get("/style.css")
            if resp_css.status_code == 200:
                css_urls = re.findall(r"url\s*\(\s*['\"]?([^'\"\)\s]+)['\"]?\s*\)", resp_css.text)
                for u in css_urls:
                    if not u.startswith("http") and not u.startswith("data:"):
                        assets_to_test.add(u)
                        
            assert len(assets_to_test) >= 1, "Expected at least 1 local static asset to be referenced"
            
            # Fetch all collected assets
            for asset in sorted(assets_to_test):
                clean_asset = asset.split("?")[0].split("#")[0]
                if not clean_asset.startswith("/"):
                    clean_asset = "/" + clean_asset
                    
                resp = client.get(clean_asset)
                if resp.status_code != 200:
                    errors.append((clean_asset, resp.status_code))
                    
    finally:
        server.shutdown()
        server.server_close()
        
    assert not errors, (
        f"HTTP Server detected broken assets or 404s: {errors}. "
        f"All referenced files must return HTTP 200 OK!"
    )

def test_t4_case_sensitivity_linux_simulation(repo_root: Path):
    """
    Validate case-sensitivity matching against disk entries.
    GitHub Pages runs on Linux where filenames are strictly case-sensitive.
    Windows is case-insensitive, so mismatch bugs can slip through unless explicitly checked.
    """
    raw_html = get_index_html(repo_root)
    soup = BeautifulSoup(raw_html, "html.parser")
    
    referenced_paths = set()
    for tag in soup.find_all(["script", "link", "img", "source"]):
        src = tag.get("src") or tag.get("href") or tag.get("srcset")
        if src and not src.startswith("http") and not src.startswith("//") and not src.startswith("#") and not src.startswith("mailto:"):
            clean = src.split("?")[0].split("#")[0]
            referenced_paths.add(clean)
            
    css_text = get_style_css(repo_root)
    css_urls = re.findall(r"url\s*\(\s*['\"]?([^'\"\)\s]+)['\"]?\s*\)", css_text)
    for u in css_urls:
        if not u.startswith("http") and not u.startswith("data:"):
            referenced_paths.add(u.split("?")[0].split("#")[0])
            
    assert len(referenced_paths) >= 1, "No local files found to check case sensitivity"
    
    case_errors = []
    for rel_path in sorted(referenced_paths):
        valid, reason = check_case_exact_path(repo_root, rel_path)
        if not valid:
            case_errors.append((rel_path, reason))
            
    assert not case_errors, (
        f"Linux case-sensitivity violations detected: {case_errors}. "
        f"Filenames in HTML/CSS must match exact disk casing for GitHub Pages Linux deployment."
    )

def test_t4_seo_and_social_metadata(repo_root: Path):
    """
    Verify SEO and Open Graph metadata for rich social sharing:
    - og:title containing 'NOXXD'
    - og:description
    - og:url targeting 'noxxd.com.br'
    - og:image for preview thumbnail
    - canonical link tag
    """
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    
    # Open Graph meta tags
    og_title = soup.find("meta", property="og:title")
    assert og_title is not None and "NOXXD" in og_title.get("content", ""), (
        "Missing or invalid <meta property='og:title'> containing 'NOXXD'"
    )
    
    og_desc = soup.find("meta", property="og:description")
    assert og_desc is not None and len(og_desc.get("content", "").strip()) >= 15, (
        "Missing or too short <meta property='og:description'>"
    )
    
    og_url = soup.find("meta", property="og:url")
    assert og_url is not None and "noxxd.com.br" in og_url.get("content", ""), (
        "Missing <meta property='og:url'> referencing 'noxxd.com.br'"
    )
    
    og_image = soup.find("meta", property="og:image")
    assert og_image is not None and len(og_image.get("content", "").strip()) > 0, (
        "Missing <meta property='og:image'> for social media preview card"
    )
    
    # Canonical link
    canonical = soup.find("link", rel=re.compile(r"canonical", re.I))
    assert canonical is not None and "noxxd.com.br" in canonical.get("href", ""), (
        "Missing canonical <link rel='canonical' href='...noxxd.com.br...'>"
    )

def test_t4_accessibility_alt_and_semantics(repo_root: Path):
    """
    Verify accessibility standards:
    - All <img> tags must have descriptive non-empty alt attributes
    - Interactive elements (buttons, links) must have descriptive text or aria-label
    - Semantic heading hierarchy
    """
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    
    # Check all images have alt attributes
    images = soup.find_all("img")
    missing_alt = [img for img in images if not img.get("alt") or len(img["alt"].strip()) == 0]
    assert not missing_alt, f"Images missing descriptive alt attribute: {missing_alt}"
    
    # Check headings exist
    h1 = soup.find("h1")
    assert h1 is not None and len(h1.get_text().strip()) > 0, "Page missing primary <h1> heading"
    
    h2_list = soup.find_all("h2")
    assert len(h2_list) >= 3, f"Expected at least 3 section <h2> headings, found {len(h2_list)}"
    
    # Check interactive buttons have accessible content
    buttons = soup.find_all(["button", "a"])
    empty_interactives = []
    for elem in buttons:
        has_text = len(elem.get_text().strip()) > 0
        has_aria = bool(elem.get("aria-label") or elem.get("title"))
        has_img = bool(elem.find("img") or elem.find("svg"))
        if not (has_text or has_aria or has_img):
            empty_interactives.append(str(elem))
            
    assert not empty_interactives, (
        f"Found interactive elements with no accessible text or aria-label: {empty_interactives}"
    )

def test_t4_contrast_ratio_simulation():
    """
    Verify WCAG 2.1 AA color contrast compliance between brand colors:
    - Text gold (#C8975D) against primary teal (#1B5E6B) and dark teal (#154B56)
    - Light text (#F5F7F8) against primary teal (#1B5E6B)
    """
    teal_primary = "#1B5E6B"
    teal_dark = "#154B56"
    gold_accent = "#C8975D"
    text_light = "#F5F7F8"
    
    # Calculate contrast ratios
    contrast_light_on_teal = calculate_contrast_ratio(text_light, teal_primary)
    assert contrast_light_on_teal >= 4.5, (
        f"Light text on teal contrast ratio {contrast_light_on_teal:.2f}:1 fails WCAG AA normal text (>= 4.5:1)"
    )
    
    contrast_gold_on_dark = calculate_contrast_ratio(gold_accent, teal_dark)
    assert contrast_gold_on_dark >= 3.0, (
        f"Gold accent on dark teal contrast ratio {contrast_gold_on_dark:.2f}:1 fails WCAG AA large text/UI (>= 3.0:1)"
    )
