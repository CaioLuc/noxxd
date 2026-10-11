"""
Pytest configuration and fixtures for NOXXD verification suite.
"""

from pathlib import Path
import pytest
from bs4 import BeautifulSoup

from tests.helpers import (
    get_repo_root,
    get_index_html,
    get_html_soup,
    get_style_css,
    get_cname,
)

@pytest.fixture(scope="session")
def repo_root() -> Path:
    """Fixture providing the root directory of the repository."""
    return get_repo_root()

@pytest.fixture
def index_html(repo_root: Path) -> str:
    """Fixture providing raw index.html text."""
    return get_index_html(repo_root)

@pytest.fixture
def html_soup(repo_root: Path) -> BeautifulSoup:
    """Fixture providing parsed index.html BeautifulSoup object."""
    return get_html_soup(repo_root)

@pytest.fixture
def style_css(repo_root: Path) -> str:
    """Fixture providing raw style.css text."""
    return get_style_css(repo_root)

@pytest.fixture
def cname_content(repo_root: Path) -> str:
    """Fixture providing raw CNAME text."""
    return get_cname(repo_root)
