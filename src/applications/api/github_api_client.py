import requests
from src.config.config import CONFIG


class GitHubApiClient:

    def __init__(self) -> None:
        self.token = None

    def search_repo(self, repo_name):
        r = requests.get(
            url=self._form_url("/search/repositories"),
            params={'q': repo_name},
            headers={"Authorization": f"Bearer {self.token}"}
            )

        if CONFIG.get("DEBUG_MODE"):
            print(r)

        return r.json()

    def login(self, username, password):
        print(f"Do login with {username}:{password}")
        #
        # DO LOGIN REQUEST
        #
        self.token = "sdkfjbkjsdf"

    def logout(self):
        print("Do logout for")

    def _form_url(self, url):
        return CONFIG.get("BASE_URL_API") + url