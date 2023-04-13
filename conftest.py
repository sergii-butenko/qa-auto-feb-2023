import pytest

from src.applications.api.github_api_client import GitHubApiClient
from src.config.config import CONFIG
from src.applications.ui.github_ui_app import GitHubUI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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


@pytest.fixture
def GitHub_UI_App():
    driver = webdriver.Chrome(
        service=Service(r"./web_drivers/chrome/chromedriver_110")
    )

    ui_app = GitHubUI(driver)

    yield ui_app

    ui_app.close()
