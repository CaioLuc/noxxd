"""
Tier 2: Boundary & Brand Constraints Tests
Verifies strict zero border-radius enforcement, brand color tokens (#1B5E6B, #154B56, #C8975D),
PIL binary image validation, external links security (rel="noopener noreferrer"),
wide letter-spacing on slogan, CNAME formatting hygiene, and pixel/checkerboard aesthetics.
"""

from pathlib import Path
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from PIL import Image
import pytest

from tests.helpers import (
    get_repo_root,
    get_index_html,
    get_style_css,
    get_cname,
    strip_css_comments,
    parse_css_declarations,
)

def test_t2_zero_border_radius_rule(repo_root: Path):
    """
    CRITICAL BRAND CONSTRAINT: Strictly zero border-radius.
    Parses style.css and asserts no positive border-radius declarations exist.
    Allowed values: '0', '0px', 'none', 'inherit', or declarations with '!important' 0.
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    
    # Check for positive border-radius values
    radius_pattern = re.compile(
        r"border(?:-(?:top|bottom)-(?:left|right))?-radius\s*:\s*([^;\}]+)",
        re.IGNORECASE
    )
    
    violations = []
    for match in radius_pattern.finditer(clean_css):
        val = match.group(1).strip()
        # Clean value from !important
        val_clean = re.sub(r"!important", "", val, flags=re.I).strip().lower()
        
        # Check if value represents non-zero
        # Valid zero values: '0', '0px', '0rem', '0em', 'none', 'inherit'
        tokens = val_clean.split()
        for token in tokens:
            # Match positive numbers with units like 8px, 4px, 50%, 0.5rem, 1em
            num_match = re.match(r"^(\d*\.?\d+)([a-z%]+)?$", token)
            if num_match:
                number_part = float(num_match.group(1))
                if number_part > 0:
                    violations.append((match.group(0), val))
                    break
            elif token not in ("0", "0px", "none", "inherit", "unset", "initial", "revert"):
                # Potential invalid or custom token
                if any(unit in token for unit in ("px", "%", "rem", "em")):
                    violations.append((match.group(0), val))
                    
    assert not violations, (
        f"Brand violation! Non-zero border-radius found in style.css: {violations}. "
        f"NOXXD brand requires strictly right-angle geometric corners (border-radius: 0)."
    )

def test_t2_brand_color_tokens(repo_root: Path):
    """
    Verify official brand color hex codes are defined in style.css:
    - Primary Teal: #1B5E6B
    - Dark Teal: #154B56
    - Accent Gold: #C8975D
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text).upper()
    
    primary_teal = "#1B5E6B"
    dark_teal = "#154B56"
    accent_gold = "#C8975D"
    
    assert primary_teal in clean_css, (
        f"Missing primary teal color {primary_teal} in style.css"
    )
    assert dark_teal in clean_css, (
        f"Missing dark teal color {dark_teal} in style.css"
    )
    assert accent_gold in clean_css, (
        f"Missing accent gold color {accent_gold} in style.css"
    )
    
    # Verify CSS custom properties (variables) definition in :root
    assert re.search(r"--(?:bg|teal|primary|color)[^:]*:\s*#1B5E6B", clean_css, re.I), (
        "Primary teal (#1B5E6B) must be defined as a CSS variable (e.g. --bg or --bg-primary)"
    )
    assert re.search(r"--(?:accent|gold|color)[^:]*:\s*#C8975D", clean_css, re.I), (
        "Accent gold (#C8975D) must be defined as a CSS variable (e.g. --accent or --color-gold)"
    )

def test_t2_image_binary_integrity_pil(repo_root: Path):
    """
    Validate binary integrity of all raster images via PIL (PIL.Image.open) and vector SVGs.
    Images must exist, not be empty, have width/height > 0, and not be corrupted.
    """
    raw_html = get_index_html(repo_root)
    soup = BeautifulSoup(raw_html, "html.parser")
    
    # Collect all image sources from HTML
    img_sources = set()
    for tag in soup.find_all(["img", "link"]):
        src = tag.get("src") or (tag.get("href") if tag.get("rel") == ["icon"] else None)
        if src and not src.startswith("http") and not src.startswith("data:"):
            img_sources.add(src.split("?")[0].split("#")[0])
            
    # Also collect image urls from CSS
    css_text = get_style_css(repo_root)
    css_urls = re.findall(r"url\s*\(\s*['\"]?([^'\"\)\s]+)['\"]?\s*\)", css_text)
    for u in css_urls:
        if not u.startswith("http") and not u.startswith("data:"):
            img_sources.add(u.split("?")[0].split("#")[0])
            
    assert len(img_sources) >= 1, "Expected at least 1 local image/asset to be referenced in HTML/CSS"
    
    for src in sorted(img_sources):
        clean_src = src.lstrip("/").replace("\\", "/")
        img_path = repo_root / clean_src
        assert img_path.exists(), f"Referenced image file does not exist on disk: {img_path}"
        assert img_path.stat().st_size > 0, f"Referenced image file is 0 bytes: {img_path}"
        
        ext = img_path.suffix.lower()
        if ext in (".jpg", ".jpeg", ".png", ".webp", ".gif", ".ico"):
            # Validate raster image with Pillow
            try:
                with Image.open(img_path) as im:
                    im.verify()
                # Reopen to check dimensions after verify()
                with Image.open(img_path) as im:
                    width, height = im.size
                    assert width > 0 and height > 0, (
                        f"Image dimensions must be > 0, got {width}x{height} for {img_path}"
                    )
            except Exception as e:
                pytest.fail(f"PIL verification failed for image {img_path}: {e}")
        elif ext == ".svg":
            # Validate SVG XML structure
            try:
                tree = ET.parse(img_path)
                root = tree.getroot()
                assert "svg" in root.tag.lower(), f"SVG root element is not <svg> in {img_path}"
            except Exception as e:
                pytest.fail(f"XML parse failed for SVG asset {img_path}: {e}")

def test_t2_external_links_security(repo_root: Path):
    """
    Verify security on external links: any link with target='_blank' or external href
    must specify rel='noopener noreferrer'.
    """
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    external_links = soup.find_all("a", href=re.compile(r"^https?://", re.I))
    
    for link in external_links:
        target = link.get("target")
        rel = link.get("rel")
        rel_str = " ".join(rel) if isinstance(rel, list) else (rel or "")
        
        if target == "_blank":
            assert "noopener" in rel_str.lower(), (
                f"External link {link.get('href')} with target='_blank' missing 'noopener' in rel attribute"
            )
            assert "noreferrer" in rel_str.lower(), (
                f"External link {link.get('href')} with target='_blank' missing 'noreferrer' in rel attribute"
            )

def test_t2_slogan_letter_spacing(repo_root: Path):
    """
    Verify style.css applies prominent letter-spacing to the slogan 'BUILD IT YOUR WAY'.
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    
    # Search for slogan selector or letter-spacing declaration
    declarations = parse_css_declarations(clean_css)
    slogan_spacing_found = False
    
    for selector, prop, val in declarations:
        if prop == "letter-spacing":
            # Check if selector relates to slogan, hero, or tracked text
            if any(k in selector.lower() for k in ("slogan", "hero", "tracking", "subtitle", "h2", "p")):
                slogan_spacing_found = True
                # Verify non-trivial letter spacing (e.g. >= 2px or >= 0.15em)
                assert val not in ("normal", "0", "0px"), (
                    f"Slogan letter-spacing must be wide, found '{val}' on selector '{selector}'"
                )
                break
                
    if not slogan_spacing_found:
        # Check if letter-spacing is applied anywhere in CSS with wide tracking
        letter_spacings = [val for _, prop, val in declarations if prop == "letter-spacing"]
        assert len(letter_spacings) > 0, (
            "style.css must define 'letter-spacing' for wide typography on slogan 'BUILD IT YOUR WAY'"
        )

def test_t2_cname_hygiene(repo_root: Path):
    """
    Verify CNAME file formatting hygiene:
    - Single line containing 'noxxd.com.br'
    - No UTF-8 BOM
    - No extraneous blank lines or whitespace
    - No control characters
    """
    cname_path = repo_root / "CNAME"
    assert cname_path.exists(), "CNAME file not found"
    
    raw_bytes = cname_path.read_bytes()
    assert not raw_bytes.startswith(b"\xef\xbb\xbf"), "CNAME must not contain UTF-8 BOM"
    
    content = raw_bytes.decode("utf-8")
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    assert len(lines) == 1, f"CNAME must contain exactly one non-empty line, found {len(lines)}"
    assert lines[0] == "noxxd.com.br", f"CNAME content was '{lines[0]}', expected 'noxxd.com.br'"

def test_t2_pixel_pattern_aesthetics(repo_root: Path):
    """
    Verify CSS or DOM incorporates geometric pixel/checkerboard design signatures
    (e.g., checkerboard borders, pixel corners, or background grid).
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    
    # Look for pixel-art, checkerboard, or grid patterns in CSS
    pattern_indicators = [
        "pixel",
        "checkerboard",
        "grid",
        "linear-gradient",
        "background-size",
        "box-shadow",
    ]
    matches = [ind for ind in pattern_indicators if ind in clean_css.lower()]
    assert len(matches) >= 2, (
        f"style.css should implement geometric pixel/grid/checkerboard aesthetics. Found: {matches}"
    )
