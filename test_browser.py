import pytest
from playwright.sync_api import sync_playwright

from pages.search_page import SearchPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page


def test_first_navigation(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    search_page = SearchPage(page)
    search_page.fill_search("playwright")
    assert search_page.get_search_text() == "playwright"