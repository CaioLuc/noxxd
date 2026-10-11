"""
Helper utilities for NOXXD 4-tier verification test suite.
"""

from pathlib import Path
import re
import os
from bs4 import BeautifulSoup
import pytest

def get_repo_root() -> Path:
    """Return repository root Path."""
    return Path(__file__).resolve().parent.parent

def get_index_html(repo_root: Path = None) -> str:
    """Read index.html from repo root or assert existence with helpful failure."""
    if repo_root is None:
        repo_root = get_repo_root()
    index_path = repo_root / "index.html"
    assert index_path.exists(), f"index.html does not exist at {index_path}"
    return index_path.read_text(encoding="utf-8", errors="replace")

def get_html_soup(repo_root: Path = None) -> BeautifulSoup:
    """Parse index.html into BeautifulSoup."""
    content = get_index_html(repo_root)
    return BeautifulSoup(content, "html.parser")

def get_style_css(repo_root: Path = None) -> str:
    """Read style.css from repo root or assert existence with helpful failure."""
    if repo_root is None:
        repo_root = get_repo_root()
    css_path = repo_root / "style.css"
    assert css_path.exists(), f"style.css does not exist at {css_path}"
    return css_path.read_text(encoding="utf-8", errors="replace")

def get_cname(repo_root: Path = None) -> str:
    """Read CNAME file from repo root or assert existence with helpful failure."""
    if repo_root is None:
        repo_root = get_repo_root()
    cname_path = repo_root / "CNAME"
    assert cname_path.exists(), f"CNAME file does not exist at {cname_path}"
    return cname_path.read_text(encoding="utf-8", errors="replace")

def strip_css_comments(css_text: str) -> str:
    """Remove CSS multi-line comments /* ... */."""
    return re.sub(r"/\*.*?\*/", "", css_text, flags=re.DOTALL)

def parse_css_declarations(css_text: str):
    """
    Parse CSS text into list of (selector, property_name, property_value).
    Strips comments and handles basic CSS structure.
    """
    clean_css = strip_css_comments(css_text)
    declarations = []
    
    # Match rule blocks: selector { ... declarations ... }
    rule_blocks = re.findall(r"([^{}]+)\{([^{}]+)\}", clean_css)
    for selector, body in rule_blocks:
        selector = selector.strip()
        # Parse property-value pairs
        for statement in body.split(";"):
            statement = statement.strip()
            if not statement or ":" not in statement:
                continue
            prop, val = statement.split(":", 1)
            declarations.append((selector, prop.strip().lower(), val.strip()))
            
    return declarations

def hex_to_rgb(hex_code: str) -> tuple[int, int, int]:
    """Convert hex color code (#RGB or #RRGGBB) to (r, g, b)."""
    hex_code = hex_code.strip().lstrip("#")
    if len(hex_code) == 3:
        hex_code = "".join([c * 2 for c in hex_code])
    if len(hex_code) != 6:
        raise ValueError(f"Invalid hex color code: #{hex_code}")
    return (int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16))

def calculate_luminance(hex_code: str) -> float:
    """Calculate relative luminance according to WCAG 2.1 specifications."""
    r, g, b = hex_to_rgb(hex_code)
    def srgb_channel(val: int) -> float:
        c = val / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    
    return 0.2126 * srgb_channel(r) + 0.7152 * srgb_channel(g) + 0.0722 * srgb_channel(b)

def calculate_contrast_ratio(hex1: str, hex2: str) -> float:
    """Calculate WCAG contrast ratio between two hex colors."""
    lum1 = calculate_luminance(hex1)
    lum2 = calculate_luminance(hex2)
    l_max = max(lum1, lum2)
    l_min = min(lum1, lum2)
    return (l_max + 0.05) / (l_min + 0.05)

def check_case_exact_path(repo_root: Path, relative_path: str) -> tuple[bool, str]:
    """
    Check if a file exists and exactly matches disk case (Linux case-sensitivity simulation).
    Returns (True, '') if valid, (False, error_reason) otherwise.
    """
    clean_rel = relative_path.split("?")[0].split("#")[0].strip()
    if clean_rel.startswith("/"):
        clean_rel = clean_rel[1:]
    
    parts = clean_rel.replace("\\", "/").split("/")
    current_dir = repo_root
    
    for part in parts:
        if not part or part == ".":
            continue
        if part == "..":
            current_dir = current_dir.parent
            continue
            
        try:
            entries = os.listdir(current_dir)
        except OSError as e:
            return False, f"Directory access error at {current_dir}: {e}"
            
        if part not in entries:
            # Check if it exists with different case
            lower_matches = [e for e in entries if e.lower() == part.lower()]
            if lower_matches:
                return False, f"Case mismatch: '{part}' requested but disk has '{lower_matches[0]}'"
            return False, f"Path segment '{part}' not found in {current_dir}"
            
        current_dir = current_dir / part
        
    return True, ""
