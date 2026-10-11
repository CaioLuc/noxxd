"""
Tier 3: Responsiveness & Micro-interactions Tests
Verifies responsive CSS media queries (320px to 1920px), horizontal overflow prevention
(overflow-x: hidden, box-sizing: border-box), button hover color inversion,
GPU-accelerated scroll reveal animations (transform, opacity), and mobile navigation adaptability.
"""

from pathlib import Path
import re
from bs4 import BeautifulSoup
import pytest

from tests.helpers import (
    get_repo_root,
    get_index_html,
    get_style_css,
    strip_css_comments,
    parse_css_declarations,
)

def test_t3_responsive_media_queries_coverage(repo_root: Path):
    """
    Verify style.css implements media queries covering responsive breakpoints:
    - Mobile: <= 768px (or 480px, 600px, 640px)
    - Tablet / Desktop transitions up to 1920px
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    
    # Find all @media declarations
    media_queries = re.findall(r"@media[^{]+\{", clean_css, re.IGNORECASE)
    assert len(media_queries) >= 1, "style.css must define responsive @media queries"
    
    # Check for mobile query targeting <= 768px (covers 320px smartphones)
    has_mobile_query = any(
        re.search(r"max-width\s*:\s*(?:768|640|600|480)px", q, re.I)
        for q in media_queries
    )
    assert has_mobile_query, (
        f"Missing mobile media query (max-width: 768px or 480px). Found queries: {media_queries}"
    )

def test_t3_horizontal_overflow_prevention(repo_root: Path):
    """
    Verify defensive rules preventing accidental horizontal scrollbar:
    - overflow-x: hidden on body, html, or main container
    - box-sizing: border-box applied globally (* or root)
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    declarations = parse_css_declarations(clean_css)
    
    # Check box-sizing: border-box
    has_border_box = any(
        prop == "box-sizing" and "border-box" in val.lower()
        for _, prop, val in declarations
    )
    assert has_border_box, "style.css must apply 'box-sizing: border-box' globally"
    
    # Check overflow-x: hidden
    has_overflow_x_hidden = any(
        prop in ("overflow-x", "overflow") and "hidden" in val.lower()
        and any(s in sel.lower() for s in ("body", "html", "container", "wrapper", "main", "*"))
        for sel, prop, val in declarations
    )
    assert has_overflow_x_hidden, (
        "style.css must define 'overflow-x: hidden' on body/html/container to prevent mobile horizontal scroll"
    )

def test_t3_button_hover_color_inversion(repo_root: Path):
    """
    Verify button hover micro-interaction:
    Buttons invert colors on :hover/:focus (gold fill -> teal fill with gold border/accent, or vice versa).
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    declarations = parse_css_declarations(clean_css)
    
    # Find hover rules targeting buttons
    button_hover_declarations = [
        (sel, prop, val) for sel, prop, val in declarations
        if ":hover" in sel.lower() and any(k in sel.lower() for k in ("btn", "button", "cta", "a."))
    ]
    assert len(button_hover_declarations) >= 1, (
        "style.css must define ':hover' micro-interaction states on buttons (.btn:hover, button:hover)"
    )
    
    # Verify color or background inversion is specified in hover declarations
    hover_props = [prop for _, prop, _ in button_hover_declarations]
    assert any(p in hover_props for p in ("background", "background-color", "color", "border", "border-color")), (
        f"Button hover rules must invert background or color/border. Found hover properties: {hover_props}"
    )

def test_t3_scroll_reveal_gpu_acceleration(repo_root: Path):
    """
    Verify scroll reveal transitions are GPU-accelerated:
    - Uses 'opacity' and 'transform' for silky 60 FPS transitions
    - Avoids animating expensive layout properties (margin, top, left, width, height)
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    declarations = parse_css_declarations(clean_css)
    
    # Find transition or animation declarations
    transition_declarations = [
        (sel, prop, val) for sel, prop, val in declarations
        if prop in ("transition", "transition-property")
    ]
    assert len(transition_declarations) >= 1, (
        "style.css must define CSS transitions for smooth micro-interactions and scroll reveals"
    )
    
    # Check for GPU-friendly properties (transform, opacity, or all with caution)
    all_transition_vals = " ".join([val for _, _, val in transition_declarations]).lower()
    has_gpu_props = "transform" in all_transition_vals or "opacity" in all_transition_vals or "all" in all_transition_vals
    assert has_gpu_props, (
        f"Transitions must animate GPU-accelerated properties ('opacity', 'transform'). Found: {all_transition_vals}"
    )
    
    # Assert expensive reflow properties are not explicitly declared as transition targets
    reflow_violators = [
        val for val in ("margin-top", "margin-left", "left", "top", "right", "bottom")
        if re.search(r"\b" + val + r"\b", all_transition_vals)
    ]
    assert not reflow_violators, (
        f"Performance hazard: expensive layout properties {reflow_violators} animated in transitions! Use 'transform' instead."
    )

def test_t3_mobile_navigation_adaptability(repo_root: Path):
    """
    Verify mobile navigation adaptability in CSS or script.js:
    - Responsive nav styling under mobile media query (e.g. flex-direction column, display toggle, menu button)
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    
    # Search for nav or menu styles inside media queries or mobile menu classes
    mobile_nav_indicators = [
        "nav",
        "menu",
        "hamburger",
        "toggle",
        "flex-direction",
    ]
    
    # Look inside media query blocks
    media_blocks = re.findall(r"@media[^{]+\{([\s\S]+?\}(?:\s*\})?)", clean_css, re.IGNORECASE)
    has_nav_media = False
    for block in media_blocks:
        if any(ind in block.lower() for ind in ("nav", "menu", "header")):
            has_nav_media = True
            break
            
    assert has_nav_media, (
        "style.css must contain responsive navigation adaptations within media queries (e.g., mobile menu stacking or toggle)"
    )

def test_t3_scroll_margin_header_offset(repo_root: Path):
    """
    Verify fixed/sticky navigation handles internal anchor scroll offsets cleanly
    (e.g., scroll-margin-top or scroll-padding-top on sections/html).
    """
    css_text = get_style_css(repo_root)
    clean_css = strip_css_comments(css_text)
    declarations = parse_css_declarations(clean_css)
    
    is_sticky_or_fixed_header = any(
        "header" in sel.lower() or "nav" in sel.lower()
        for sel, prop, val in declarations
        if prop == "position" and any(p in val.lower() for p in ("fixed", "sticky"))
    )
    
    if is_sticky_or_fixed_header:
        has_scroll_offset = any(
            prop in ("scroll-margin-top", "scroll-padding-top", "scroll-margin")
            for _, prop, _ in declarations
        )
        assert has_scroll_offset, (
            "Header is fixed/sticky: style.css must define 'scroll-margin-top' or 'scroll-padding-top' "
            "so anchor navigation does not hide section titles behind the navbar"
        )
