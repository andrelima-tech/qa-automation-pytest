from playwright.sync_api import sync_playwright


def test_first_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")

        assert "Google" in page.title()
        search_box = page.locator('[name="q"]')
        assert search_box.is_visible()