
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class BrowsersProvider:

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
        elif browser_name == 'ie'
            options = None
            
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
            
        else:
            raise NotImplementedError(f"Browser name {browser_name} is not supported for UI tests. Please register it in BrowsersProvider class")

        return driver
