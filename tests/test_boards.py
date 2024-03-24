import pytest
from playwright.sync_api import expect

from test_data import generate_test_data

BOARD_TITLES = []


@pytest.fixture()
def cleanup_boards(auth_app):
    yield
    for board_title in BOARD_TITLES:
        auth_app.home_page.delete_board(board_title)
    expect(auth_app.home_page.header_component.board_title_fade).to_have_count(
        0
    )  # if account is new, it will be empty


@pytest.mark.usefixtures("cleanup_boards")
class TestBoards:

    @pytest.mark.parametrize(
        "board_title",
        [
            pytest.param(
                generate_test_data.random_string(),
                id="Title as string",
            ),
            pytest.param(
                generate_test_data.random_integer(),
                id="Title as integer",
            ),
            pytest.param(
                generate_test_data.special_symbols(),
                id="Title as special symbols",
            ),
        ],
    )
    def test_create_board(self, auth_app, board_title) -> None:
        BOARD_TITLES.append(board_title)
        auth_app.home_page.create_board(board_title)

        expect(auth_app.home_page.header_component.board_name_container).to_have_text(
            str(board_title)
        )
