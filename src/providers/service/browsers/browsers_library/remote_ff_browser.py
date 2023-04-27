from selenium import webdriver
from src.config.config import CONFIG


class RemoteFF:

    @staticmethod
    def get_driver():
        options = webdriver.FirefoxOptions()
        # options.set_capability("browserVersion", "67")
        # options.set_capability("platformName", "Windows XP")

        driver = webdriver.Remote(
            command_executor=CONFIG.get("SELENIUM_GRID_URL"),
            options=options
        )

        return driver
