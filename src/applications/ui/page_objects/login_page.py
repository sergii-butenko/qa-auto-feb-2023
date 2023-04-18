from src.config.config import CONFIG
from selenium.webdriver.common.by import By
import time


class LoginPage:
    URL = "/login"

    USERNAME_FLD = "login_field" #id
    PASSWROD_FLD = "password" #id
    SIGN_IN_BTN = "commit" #name

    def __init__(self, app) -> None:
        self.driver = self.app.driver

    def go_to(self):
        self.app.driver.get(CONFIG.get("BASE_URL_UI") + LoginPage.URL)

    def try_sign_in(self, username, password):
        username_fld = self.app.driver.find_element(By.ID, LoginPage.USERNAME_FLD)
        username_fld.send_keys(username)

        password_fld = self.app.driver.find_element(By.ID, LoginPage.PASSWROD_FLD)
        password_fld.send_keys(password)

        sign_in_btn = self.app.driver.find_element(By.NAME, LoginPage.SIGN_IN_BTN)
        sign_in_btn.click()

        time.sleep(5)

        return self

    def click_sign_up_page(self):
        sing_up_page = self.app.SignUpPage(self.app)
        sing_up_page.wait_loaded()

        return sing_up_page

    def go_to_forgot_pass_page(self):
        # return any
        pass

    def check_error_message(self):
        # return bool

        # if error exists - return True
        # else - return False
        # error_msg = self.driver.find_element(By.ID, LoginPage.USERNAME_FLD)
        error_msg = "Error"
        return error_msg == "Error"