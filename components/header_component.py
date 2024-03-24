from playwright.sync_api import Page


class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page
        self.header_container = page.get_by_test_id("header-container")
        self.member_menu = page.get_by_test_id("header-member-menu-avatar")
        self.login_button = page.locator("//*[contains(@data-uuid, 'login')]")
        self.logout_button = page.get_by_test_id("account-menu-logout")
        self.submit_logout_button = page.locator("#logout-submit")
        # TODO: Move board locators to a separate module.
        self.create_menu_button = page.get_by_test_id("header-create-menu-button")
        self.create_board_button = page.get_by_test_id("header-create-board-button")
        self.create_board_popover = page.get_by_test_id("header-create-menu-popover")
        self.create_board_input = page.get_by_test_id("create-board-title-input")
        self.create_board_submit_button = page.get_by_test_id(
            "create-board-submit-button"
        )
        self.board_name_container = page.get_by_test_id("board-name-container")
        self.boards_link = page.get_by_test_id("open-boards-link")
        self.board_title_fade = page.locator("#board-tile-fade")
