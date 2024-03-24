from playwright.sync_api import Page

from components.header_component import HeaderComponent


class HomePage:
    __url: str = "https://trello.com"

    def __init__(self, page: Page):
        self.page = page
        self.header_component = HeaderComponent(page)

    def navigate_to_home_page(self):
        self.page.goto(self.__url)
        self.page.wait_for_load_state()

    def logout_user(self):
        self.header_component.member_menu.click()
        self.header_component.logout_button.click()
        self.header_component.submit_logout_button.click()
        self.page.wait_for_load_state()

    def create_board(self, title):
        self.header_component.create_menu_button.click()
        self.header_component.create_board_button.click()
        self.header_component.create_board_input.fill(str(title))
        self.header_component.create_board_submit_button.click()
        self.page.wait_for_load_state()

    def choose_board_by_title(self, title):
        self.header_component.boards_link.click()
        self.page.locator(f"div[title='{str(title)}']").click()

    def delete_board(self, title):
        self.choose_board_by_title(title)
        # TODO: Move locators to constructor BoardPage
        self.page.get_by_label("Show menu").click()
        self.page.locator("//*[contains(@class, 'js-close-board')]").click()
        self.page.get_by_test_id("close-board-confirm-button").click()
        self.page.get_by_test_id("close-board-delete-board-button").click()
        self.page.get_by_test_id("close-board-delete-board-confirm-button").click()
