"""
Tier 1: Feature & Structural Coverage Tests
Verifies existence of root deployment files, CNAME exact content, HTML5 semantic DOM,
5 primary sections with matching anchor IDs, 3 services cards, real projects (Urbis, HealthSearch,
CARITAS) portfolio, contact channels, strict brand orthography ('NOXXD' vs 'NOXXED'),
slogan 'BUILD IT YOUR WAY', and footer copyright.
"""

from pathlib import Path
import re
from bs4 import BeautifulSoup
import pytest

from tests.helpers import get_repo_root, get_index_html, get_cname

def test_t1_root_deployment_files_exist(repo_root: Path):
    """Verify presence of core deployment files at repository root."""
    required_files = ["CNAME", "index.html", "style.css"]
    missing = [f for f in required_files if not (repo_root / f).exists()]
    assert not missing, f"Missing required root deployment files: {missing}"

def test_t1_cname_content_exact(repo_root: Path):
    """Verify CNAME file contains strictly 'noxxd.com.br' without protocol or whitespace."""
    cname_text = get_cname(repo_root).strip()
    assert cname_text == "noxxd.com.br", (
        f"CNAME content mismatch. Expected 'noxxd.com.br', got '{cname_text}'"
    )
    assert not cname_text.startswith("http"), "CNAME must not include http/https protocol"
    assert not cname_text.startswith("www."), "CNAME root domain should not include 'www.'"

def test_t1_html5_semantic_structure(repo_root: Path):
    """Verify semantic HTML5 structure: DOCTYPE, html lang, head, body, header, main, footer."""
    raw_html = get_index_html(repo_root)
    assert re.search(r"<!DOCTYPE\s+html>", raw_html, re.IGNORECASE), "Missing <!DOCTYPE html> declaration"
    
    soup = BeautifulSoup(raw_html, "html.parser")
    html_tag = soup.find("html")
    assert html_tag is not None, "Missing <html> root element"
    lang = html_tag.get("lang", "")
    assert lang.lower().startswith("pt"), f"Expected html lang to be Portuguese (pt-BR or pt), got '{lang}'"
    
    assert soup.find("head") is not None, "Missing <head> element"
    assert soup.find("body") is not None, "Missing <body> element"
    assert soup.find("header") is not None, "Missing semantic <header> element"
    assert soup.find("main") is not None, "Missing semantic <main> element"
    assert soup.find("footer") is not None, "Missing semantic <footer> element"

def test_t1_meta_viewport_and_charset(repo_root: Path):
    """Verify presence of charset and responsive viewport meta tags."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    
    charset_meta = soup.find("meta", charset=True)
    if not charset_meta:
        charset_meta = soup.find("meta", attrs={"http-equiv": re.compile(r"content-type", re.I)})
        assert charset_meta and "utf-8" in charset_meta.get("content", "").lower(), "Missing UTF-8 charset meta tag"
    else:
        assert charset_meta["charset"].lower() == "utf-8", (
            f"Expected charset UTF-8, got '{charset_meta['charset']}'"
        )
        
    viewport_meta = soup.find("meta", attrs={"name": "viewport"})
    assert viewport_meta is not None, "Missing <meta name='viewport'> tag"
    viewport_content = viewport_meta.get("content", "")
    assert "width=device-width" in viewport_content, "Viewport meta must contain 'width=device-width'"
    assert "initial-scale=1" in viewport_content, "Viewport meta must contain 'initial-scale=1'"

def test_t1_page_title_and_meta_description(repo_root: Path):
    """Verify page title contains 'NOXXD' and meta description is present."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    
    title_tag = soup.find("title")
    assert title_tag is not None and title_tag.string, "Missing or empty <title> tag"
    assert "NOXXD" in title_tag.string, f"<title> must include 'NOXXD', found: '{title_tag.string}'"
    
    desc_meta = soup.find("meta", attrs={"name": "description"})
    assert desc_meta is not None, "Missing <meta name='description'> tag"
    assert len(desc_meta.get("content", "").strip()) >= 15, "Meta description is too short or empty"

def test_t1_primary_sections_and_anchors(repo_root: Path):
    """Verify 5 primary sections exist (#inicio/#hero, #servicos, #projetos, #contato, footer) and nav anchors resolve."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    
    # Check sections existence
    hero_section = soup.find(id=re.compile(r"^(inicio|hero)$", re.I))
    assert hero_section is not None, "Missing hero section with id='inicio' or id='hero'"
    
    servicos_section = soup.find(id=re.compile(r"^servicos$", re.I))
    assert servicos_section is not None, "Missing services section with id='servicos'"
    
    projetos_section = soup.find(id=re.compile(r"^projetos$", re.I))
    assert projetos_section is not None, "Missing portfolio section with id='projetos'"
    
    contato_section = soup.find(id=re.compile(r"^contato$", re.I))
    assert contato_section is not None, "Missing contact section with id='contato'"
    
    footer_element = soup.find("footer")
    assert footer_element is not None, "Missing semantic <footer> element"
    
    # Check all internal navigation anchor links resolve to elements with matching ID
    nav = soup.find("nav")
    assert nav is not None, "Missing <nav> element for navigation"
    nav_links = nav.find_all("a", href=re.compile(r"^#.+"))
    assert len(nav_links) >= 3, f"Expected at least 3 internal nav links, found {len(nav_links)}"
    
    for link in nav_links:
        target_id = link["href"].lstrip("#")
        target_elem = soup.find(id=target_id)
        assert target_elem is not None, f"Nav link {link['href']} does not match any element with id='{target_id}'"

def test_t1_services_section_cards(repo_root: Path):
    """Verify #servicos contains 3 distinct service offerings: Sites/Landing Pages, Sistemas Web/SaaS, Consultoria."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    servicos_section = soup.find(id=re.compile(r"^servicos$", re.I))
    assert servicos_section is not None, "Missing #servicos section"
    
    servicos_text = servicos_section.get_text()
    
    # 1. Sites / Landing Pages
    assert re.search(r"(sites|landing\s+pages)", servicos_text, re.I), (
        "Services section missing 'Criação de Sites e Landing Pages' card/offering"
    )
    # 2. Sistemas Web / SaaS
    assert re.search(r"(sistemas\s+web|saas|aplicativos)", servicos_text, re.I), (
        "Services section missing 'Sistemas Web e SaaS / Aplicativos' card/offering"
    )
    # 3. Consultoria em Tecnologia
    assert re.search(r"consultoria", servicos_text, re.I), (
        "Services section missing 'Consultoria em Tecnologia' card/offering"
    )
    
    # Verify structured items (cards or list items)
    cards = servicos_section.select(".service-card, .card, [class*='service'], li, article")
    assert len(cards) >= 3, f"Expected at least 3 service cards/items in #servicos, found {len(cards)}"

def test_t1_portfolio_real_projects(repo_root: Path):
    """Verify #projetos shows the 3 real projects (Urbis replaced Cidadão Relata) with logo, link and metric."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    projetos_section = soup.find(id=re.compile(r"^projetos$", re.I))
    assert projetos_section is not None, "Missing #projetos section"

    cards = projetos_section.select("article.project-card")
    assert len(cards) == 3, f"Expected exactly 3 project cards, found {len(cards)}"

    expected = [
        ("Urbis", "projetos/urbis/", "assets/projetos/urbis/logo.png"),
        ("HealthSearch", "projetos/healthsearch/", "assets/projetos/healthsearch/logo.png"),
        ("CARITAS", "projetos/caritas/", "assets/projetos/caritas/logo.svg"),
    ]
    for card, (name, href, logo) in zip(cards, expected):
        assert card.find("h3").get_text(strip=True) == name, f"Card order/name mismatch for {name}"
        assert card.find("img", src=logo) is not None, f"{name} card must use official logo {logo}"
        assert card.find("a", href=href) is not None, f"{name} card must link to {href}"
        assert card.select_one(".project-metric strong").get_text(strip=True), f"{name} card needs an impact metric"
        assert len(card.select(".tag")) >= 2, f"{name} card needs category badges"
        assert len(card.select_one(".project-summary").get_text(strip=True)) > 40, f"{name} card needs a summary"

    text = projetos_section.get_text()
    assert "Cidadão Relata" not in text, "Cidadão Relata was renamed to Urbis"
    for placeholder in ("Portal da Transparência", "GeoUrban", "AtendeCidadão"):
        assert placeholder not in text, f"Placeholder project '{placeholder}' must be gone"

def test_t1_portfolio_modular_grid(repo_root: Path):
    """Verify #projetos has modular portfolio structure with multiple projects."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    projetos_section = soup.find(id=re.compile(r"^projetos$", re.I))
    assert projetos_section is not None, "Missing #projetos section"
    
    # Check for additional project cards/items
    project_items = projetos_section.select(".project-card, .portfolio-card, [class*='project'], article, .card")
    assert len(project_items) >= 2, (
        f"Expected modular project grid with at least 2 project cards in #projetos, found {len(project_items)}"
    )

def test_t1_contact_channels(repo_root: Path):
    """Verify #contato contains direct email mailto:contato@noxxd.com.br and communication links."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    contato_section = soup.find(id=re.compile(r"^contato$", re.I))
    assert contato_section is not None, "Missing #contato section"
    
    # Check email mailto link
    email_link = contato_section.find("a", href=re.compile(r"^mailto:contato@noxxd\.com\.br", re.I))
    assert email_link is not None, (
        "Missing email link href='mailto:contato@noxxd.com.br' in #contato"
    )
    
    # Check communication channel links (WhatsApp, phone, or contact CTA)
    all_contact_links = contato_section.find_all("a")
    assert len(all_contact_links) >= 1, "Expected contact channel links in #contato"

def test_t1_brand_name_strict_orthography(repo_root: Path):
    """Verify brand is strictly spelled 'NOXXD' with zero occurrences of 'NOXXED' across the document."""
    raw_html = get_index_html(repo_root)
    
    # Disallowed spelling check (case-insensitive)
    noxxed_matches = re.findall(r"NOXXED", raw_html, re.IGNORECASE)
    assert len(noxxed_matches) == 0, (
        f"Forbidden brand misspelling 'NOXXED' found {len(noxxed_matches)} times in index.html! Brand must strictly be 'NOXXD'."
    )
    
    # Allowed spelling presence
    noxxd_matches = re.findall(r"NOXXD", raw_html)
    assert len(noxxd_matches) >= 3, (
        f"Brand 'NOXXD' should appear prominently (at least 3 times) in index.html, found {len(noxxd_matches)}"
    )

def test_t1_brand_slogan_exact(repo_root: Path):
    """Slogan is bilingual: 'CONSTRUA DO SEU JEITO' (PT, default in index.html) / 'BUILD IT YOUR WAY' (EN dictionary)."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    slogan = soup.find(attrs={"data-i18n": "hero_slogan"})
    assert slogan is not None and slogan.get_text(strip=True) == "CONSTRUA DO SEU JEITO", "PT slogan missing in hero"
    js = (repo_root / "script.js").read_text(encoding="utf-8")
    assert 'hero_slogan: "CONSTRUA DO SEU JEITO"' in js and 'hero_slogan: "BUILD IT YOUR WAY"' in js, (
        "Slogan must be translated in both i18n dictionaries"
    )

def test_t1_footer_copyright(repo_root: Path):
    """Verify footer contains 'NOXXD' and copyright reference."""
    soup = BeautifulSoup(get_index_html(repo_root), "html.parser")
    footer = soup.find("footer")
    assert footer is not None, "Missing <footer> element"
    footer_text = footer.get_text()
    assert "NOXXD" in footer_text, f"Footer must mention 'NOXXD', got: '{footer_text.strip()}'"
    assert re.search(r"(2026|direitos|todos\s+os\s+direitos|&copy;|©)", footer_text, re.I), (
        "Footer must contain copyright notice"
    )
