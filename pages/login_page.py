from dotenv import load_dotenv
import os
from playwright.sync_api import Page

from pages.home_page import HomePage

# Load environment variables from .env file
load_dotenv()


class LoginPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("#login-submit")

    def fill_username_input(self, username: str = os.getenv("USERNAME")):
        self.username_input.fill(username)

    def fill_password_input(self, password: str = os.getenv("PASSWORD")):
        self.password_input.fill(password)

    def click_submit_button(self):
        self.submit_button.click()
        self.page.wait_for_load_state()

    def login_as_test_user(self):
        self.navigate_to_home_page()
        self.header_component.login_button.click()
        self.fill_username_input(os.getenv("USERNAME"))
        self.click_submit_button()
        self.fill_password_input(os.getenv("PASSWORD"))
        self.click_submit_button()
        self.page.wait_for_load_state()
