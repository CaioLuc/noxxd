"""
Tier 5: Project Case Pages (/projetos/<slug>/)
Verifies the 3 dedicated pages (Urbis, HealthSearch, CARITAS): HTTP 200 on clean routes, zero broken
internal links/assets across Home + project pages, official logos, descriptive copy, pinned palettes
and typography, PT/EN switch, NOXXD frame (back link, contact, footer), 8-bit particles, CNAME and
JavaScript syntax via `node --check`.
"""

from pathlib import Path
import re
import shutil
import subprocess
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
import httpx
import pytest

from tests.helpers import get_cname, get_style_css, check_case_exact_path
from tests.test_tier4_deploy import find_free_port

PROJECTS = {
    "urbis": {
        "name": "Urbis",
        "logo": "assets/projetos/urbis/logo.png",
        "colors": ["#03045E", "#243d80", "#0077B6", "#00B4D8", "#CAF0F8", "#FFFFFF", "#F8FAFC"],
        "fonts": ["Manrope", "Inter"],
        "terms": [r"Expo SDK 54", r"Next\.js 14", r"Leaflet", r"Recharts", r"Defesa Civil",
                  r"mapa de calor", r"geolocaliza", r"Lei 14\.129/2021", r"LGPD", r"tur[íi]stic"],
    },
    "healthsearch": {
        "name": "HealthSearch",
        "logo": "assets/projetos/healthsearch/logo.png",
        "colors": ["#0B2545", "#13375e", "#F5A623", "#f4f6f8", "#ffffff", "#16a34a", "#d97706", "#dc2626"],
        "fonts": ["Archivo"],
        "terms": [r"SIGAC", r"NR-07", r"NR-01", r"NR-35", r"absente[íi]smo", r"folha", r"CID-10",
                  r"AES-GCM", r"256 bits", r"React 19", r"Tailwind v4", r"Firebase", r"Cloudflare R2", r"egress"],
    },
    "caritas": {
        "name": "CARITAS",
        "logo": "assets/projetos/caritas/logo.svg",
        "colors": ["#0A1628", "#2563EB", "#F8F9FA", "#0D1117", "#EFF6FF"],
        "fonts": ["Sora", "Inter"],
        "terms": [r"[Pp]rontu[áa]rio", r"[Aa]namnese", r"question[áa]rio", r"GPT-4o-mini", r"06/2019",
                  r"/agendar/:slug", r"PIX", r"QR Code", r"Copia e Cola", r"5 anos", r"anonimiza", r"LGPD"],
    },
}


def read_page(repo_root: Path, slug: str) -> str:
    path = repo_root / "projetos" / slug / "index.html"
    assert path.exists(), f"Missing project page {path}"
    return path.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def site(repo_root: Path):
    """Ephemeral static server over the repo root, simulating GitHub Pages."""
    port = find_free_port()
    handler = partial(SimpleHTTPRequestHandler, directory=str(repo_root))
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}"
    with httpx.Client(base_url=base, timeout=5.0) as client:
        yield base, client
    server.shutdown()
    server.server_close()


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_clean_route_returns_200(site, slug: str):
    _, client = site
    resp = client.get(f"/projetos/{slug}/")
    assert resp.status_code == 200, f"/projetos/{slug}/ returned HTTP {resp.status_code}"
    assert PROJECTS[slug]["name"] in resp.text


def test_t5_zero_broken_internal_links(site):
    """Crawl Home + 3 project pages: every internal href/src returns 200 and every #fragment exists."""
    base, client = site
    pages = ["/"] + [f"/projetos/{slug}/" for slug in PROJECTS]
    soups = {}
    errors = []

    def soup_for(path: str) -> BeautifulSoup:
        if path not in soups:
            soups[path] = BeautifulSoup(client.get(path).text, "html.parser")
        return soups[path]

    for page in pages:
        soup = soup_for(page)
        refs = [t.get("href") for t in soup.find_all(["a", "link"], href=True)]
        refs += [t.get("src") for t in soup.find_all(["img", "script"], src=True)]
        for ref in refs:
            if ref.startswith(("mailto:", "tel:", "data:")):
                continue
            url = urlparse(urljoin(base + page, ref))
            if url.netloc != urlparse(base).netloc:
                continue
            target = url.path or "/"
            resp = client.get(target)
            if resp.status_code != 200:
                errors.append((page, ref, resp.status_code))
                continue
            if url.fragment and target.endswith("/"):
                if soup_for(target).find(id=url.fragment) is None:
                    errors.append((page, ref, f"missing #{url.fragment}"))

    assert not errors, f"Broken internal links/assets: {errors}"


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_local_paths_match_disk_case(repo_root: Path, slug: str):
    soup = BeautifulSoup(read_page(repo_root, slug), "html.parser")
    page_dir = f"projetos/{slug}/"
    problems = []
    for tag in soup.find_all(["img", "script", "link", "a"]):
        ref = tag.get("src") or tag.get("href")
        if not ref or ref.startswith(("http", "#", "mailto:", "//")):
            continue
        resolved = urlparse(urljoin("https://noxxd.com.br/" + page_dir, ref)).path.lstrip("/")
        if not resolved or resolved.endswith("/"):
            resolved += "index.html"
        ok, reason = check_case_exact_path(repo_root, resolved)
        if not ok:
            problems.append((ref, reason))
    assert not problems, f"Case/path problems on {slug}: {problems}"


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_official_logo_rendered(repo_root: Path, slug: str):
    meta = PROJECTS[slug]
    soup = BeautifulSoup(read_page(repo_root, slug), "html.parser")
    logo = soup.find("img", src=f"../../{meta['logo']}")
    assert logo is not None, f"{slug} page must render its official logo {meta['logo']}"
    assert meta["name"].lower() in logo.get("alt", "").lower(), "Logo alt text must name the project"
    assert logo.get("width") and logo.get("height"), "Logo needs intrinsic size to avoid layout shift"
    assert (repo_root / meta["logo"]).stat().st_size > 1000, "Logo file looks empty"


def test_t5_raster_logos_have_real_transparency(repo_root: Path):
    """The source PNGs had a fake checkerboard baked in; shipped logos must be true RGBA."""
    from PIL import Image
    for slug in ("urbis", "healthsearch"):
        img = Image.open(repo_root / PROJECTS[slug]["logo"])
        assert img.mode == "RGBA", f"{slug} logo must be RGBA"
        assert img.getpixel((0, 0))[3] == 0, f"{slug} logo corner must be transparent"


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_descriptive_copy(repo_root: Path, slug: str):
    text = BeautifulSoup(read_page(repo_root, slug), "html.parser").get_text(" ")
    missing = [t for t in PROJECTS[slug]["terms"] if not re.search(t, text)]
    assert not missing, f"{slug} page missing descriptive content: {missing}"


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_pinned_palette_and_typography(repo_root: Path, slug: str):
    html = read_page(repo_root, slug)
    style = "".join(s.get_text() for s in BeautifulSoup(html, "html.parser").find_all("style")).lower()
    missing = [c for c in PROJECTS[slug]["colors"] if c.lower() not in style]
    assert not missing, f"{slug} page missing palette tokens: {missing}"
    for font in PROJECTS[slug]["fonts"]:
        assert f"family={font}" in html, f"{slug} page must load font {font}"
        assert f"'{font.lower()}'" in style, f"{slug} page must use font {font} in CSS"


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_noxxd_frame_and_cta(repo_root: Path, slug: str):
    soup = BeautifulSoup(read_page(repo_root, slug), "html.parser")
    bar = soup.find("header", class_="nx-bar")
    assert bar is not None, "Missing NOXXD top bar"
    back = bar.find("a", class_="nx-back")
    assert back is not None and back["href"] == "../../" and "NOXXD Home" in back.get_text(), "Back link to Home broken"
    assert bar.find("a", href="../../#contato") is not None, "Top bar needs a contact button"
    ctas = soup.select("main a.p-btn[href='../../#contato']")
    assert len(ctas) >= 2, "Need a hero CTA and a closing CTA to /#contato"
    footer = soup.find("footer", class_="nx-footer")
    assert footer is not None and "NOXXD" in footer.get_text() and "BUILD IT YOUR WAY" in footer.get_text()
    assert soup.find("main") is not None and soup.find("h1") is not None
    assert len(soup.find_all("h1")) == 1, "Exactly one h1 per page"


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_bilingual_pt_en(repo_root: Path, slug: str):
    html = read_page(repo_root, slug)
    soup = BeautifulSoup(html, "html.parser")
    assert soup.html.get("lang") == "pt-BR", "Portuguese must be the default language"
    assert soup.html.get("data-title-en"), "English document title missing"
    langs = {b.get("data-lang") for b in soup.select("button.lang-btn")}
    assert langs == {"pt", "en"}, "PT | EN switch buttons missing"
    pt = soup.select('main [lang="pt-BR"]')
    en = soup.select('main [lang="en"]')
    assert len(pt) >= 40 and len(pt) == len(en), f"Unbalanced translations: {len(pt)} PT vs {len(en)} EN"
    assert soup.find("script", src="../projeto.js") is not None, "Language script not loaded"


@pytest.mark.parametrize("slug", PROJECTS)
def test_t5_screenshot_slots(repo_root: Path, slug: str):
    soup = BeautifulSoup(read_page(repo_root, slug), "html.parser")
    assert len(soup.select("figure.shot .shot__screen")) >= 2, "Need framed screenshot slots"
    assert (repo_root / "assets" / "projetos" / slug / "screens").is_dir(), "screens/ folder for future prints missing"


def test_t5_home_particles_gpu_and_reduced_motion(repo_root: Path):
    css = get_style_css(repo_root)
    js = (repo_root / "script.js").read_text(encoding="utf-8")
    assert ".pixel-field" in css and "translate3d" in css, "Particles must animate with translate3d"
    block = re.search(r"@keyframes pixel-float\s*\{(.*?)\n\}", css, re.S)
    assert block and not re.search(r"\b(top|left|margin|width|height)\s*:", block.group(1)), (
        "Particle keyframes must only animate transform"
    )
    assert re.search(r"prefers-reduced-motion: reduce\)\s*\{\s*\.pixel-field\s*\{\s*display:\s*none", css), (
        "Particles must be hidden under prefers-reduced-motion"
    )
    assert "pixel-field" in js and "prefersReducedMotion" in js, "script.js must build the particle field"


def test_t5_cname_preserved(repo_root: Path):
    assert get_cname(repo_root).strip() == "noxxd.com.br"


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
@pytest.mark.parametrize("script", ["script.js", "projetos/projeto.js"])
def test_t5_node_syntax_check(repo_root: Path, script: str):
    result = subprocess.run(["node", "--check", str(repo_root / script)], capture_output=True, text=True)
    assert result.returncode == 0, f"node --check {script} failed: {result.stderr}"
