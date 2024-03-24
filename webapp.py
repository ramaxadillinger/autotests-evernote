from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage


class WebApp:
    def __init__(self, page: Page):
        self.page: Page = page
        self.home_page: HomePage = HomePage(page)
        self.login_page: LoginPage = LoginPage(page)
