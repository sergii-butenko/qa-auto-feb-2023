import pytest

from src.applications.api.github_api_client import GitHubApiClient
from src.config.config import CONFIG
from src.applications.ui.github_ui_app import GitHubUI
from src.providers.service.browsers.browsers_provider import BrowsersProvider


class User:
    def __init__(self, age) -> None:
        # datadabase interaction
        self.age = age

    def remove(self):
        # database interaction
        self.age = None


@pytest.fixture(scope="session")
def user():
    # before test
    print("Create user")
    user = User(42)

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()


@pytest.fixture
def github_api_client():
    github_api_client = GitHubApiClient()
    github_api_client.login(CONFIG.get("USERNAME"), CONFIG.get("PASSWORD"))

    yield github_api_client

    github_api_client.logout()


@pytest.fixture(scope='session')
def github_ui_app():
    browser = CONFIG.get("BROWSER")
    driver = BrowsersProvider.get_driver(browser)

    ui_app = GitHubUI(driver)

    yield ui_app

    ui_app.quit()
