class SearchPage:
    SEARCH_BOX = '[name="q"]'

    def __init__(self, page):
        self.page = page

    def fill_search(self, text):
        self.page.locator(self.SEARCH_BOX).fill(text)

    def get_search_text(self):
        return self.page.locator(self.SEARCH_BOX).input_value()
