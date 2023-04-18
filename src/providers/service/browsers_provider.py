from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options


class BrowsersProvider:

    # BROWSER_MAPPER = {
    #     'chrome': 
    # }


    def get_driver(browser_name):
        """
        browser_name -> 'chrome, ff, edge'
        """

        if browser_name == 'chrome':
            options = Options()
            options.page_load_strategy = 'normal'

            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser_name == 'ff':
            options = None
            
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        else:
            raise NotImplementedError(f"Browser name {browser_name} is not supported for UI tests. Please register it in BrowsersProvider class")

        return driver
