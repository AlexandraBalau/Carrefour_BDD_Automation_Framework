from browser import Browser
from pages.base_page import BasePage
from pages.career_page import CareerPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.searched_products_page import SearchedProductsPage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()
    context.forgot_password_page = ForgotPasswordPage()
    context.home_page = HomePage()
    context.searched_products_page = SearchedProductsPage()
    context.career_page = CareerPage()


def after_all(context):
    context.browser.close()
