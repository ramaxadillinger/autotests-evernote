from playwright.sync_api import expect
from test_data import generate_test_data


def test_is_login_successful(app):
    app.home_page.navigate_to_home_page()
    app.home_page.header_component.login_button.click()
    app.login_page.fill_username_input()
    app.login_page.click_submit_button()
    app.login_page.fill_password_input()
    app.login_page.click_submit_button()

    expect(app.page).to_have_title("Boards | Trello")


def test_is_login_unsuccessful(app):
    app.home_page.navigate_to_home_page()
    app.home_page.header_component.login_button.click()
    app.login_page.fill_username_input(generate_test_data.email())
    app.login_page.click_submit_button()
    app.login_page.fill_password_input(generate_test_data.random_string())
    app.login_page.click_submit_button()

    expect(app.page).not_to_have_title("Boards | Trello")
