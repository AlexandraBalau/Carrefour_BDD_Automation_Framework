from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    LOGO_IMG = (By.XPATH, '//img[@class="navbar-logo"]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="search"]')
    SEARCH_BTN = (By.XPATH, '//button[@class="form-submit"]')
    MENU_BTN = (By.XPATH, '//button[@id="burger-main-menu-toggle"]')

    def navigate_to_home_page(self):
        sleep(5)
        self.driver.get('https://carrefour.ro/')

    def click_logo_img(self):
        sleep(1)
        self.driver.find_element(*self.LOGO_IMG).click()

    def search_after(self, query):
        sleep(1)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(query)

    def click_search_btn(self):
        self.driver.find_element(*self.SEARCH_BTN).click()
        sleep(1)

    def verify_page_url(self, expected_url):
        sleep(1)
        actual = self.driver.current_url
        assert actual == expected_url, f'URL este gresit'

    def click_menu_btn(self):
        sleep(1)
        self.driver.find_element(*self.MENU_BTN).click()

    def hover_over_menu_category(self, category_name):
        sleep(1)
        elem = self.driver.find_element(By.XPATH, f'(//li[@class="level-0 has-dropdown"])')
        self.hover_by_elem(elem)

    def hover_over_menu_subcategory(self, subcategory_name):
        sleep(1)
        elem = self.driver.find_element(By.XPATH, f'(//span[normalize-space()=""])')
        self.hover_by_elem(elem)



