from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchedProductsPage(BasePage):
    RESULTS_TITLE = (By.PARTIAL_LINK_TEXT, 'https://carrefour.ro/produse/')

    def verify_results_contain_text(self, text):
        title_list = self.driver.find_elements(*self.RESULTS_TITLE)
        for element in title_list:
            title = element.text.lower()
            assert text in title, f'Result does not contain search query'
