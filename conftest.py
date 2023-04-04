import pytest

from src.applications.api.github_api_client import GitHubApiClient
from src.config.config import config


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
    github_api_client.login(config.get("USERNAME"), config.get("PASSWORD"))

    yield github_api_client

    github_api_client.logout()
