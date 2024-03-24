import pytest

from webapp import WebApp


@pytest.fixture()
def app(page) -> WebApp:
    return WebApp(page)


@pytest.fixture()
def auth_app(app) -> WebApp:
    app.login_page.login_as_test_user()
    yield app
    app.home_page.logout_user()
