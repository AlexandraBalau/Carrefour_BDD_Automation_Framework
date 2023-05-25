from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CareerPage(BasePage):

    CAREER_LNK = (By.XPATH, '//div[@class="navbar-container catalogues-container"]')
    CITY = (By.XPATH, '//select[@id="city"]')
    STORE = (By.XPATH, '//select[@id="store"]')
    SEARCH_JOB_BUTTON = (By.XPATH, '//button[contains(text(),"Caută un job")]')

    def navigate_to_home_page(self):
        self.driver.get('https://carrefour.ro/')

    def click_career_lnk(self):
        self.driver.find_element(*self.CAREER_LNK).click()

    def search_city(self, city):
        sleep(3)
        self.driver.find_element(*self.CITY).send_keys(city)

    def search_store(self, store):
        self.driver.find_element(*self.STORE).send_keys(store)

    def click_search_job_button(self):
        self.driver.find_element(*self.SEARCH_JOB_BUTTON).click()
