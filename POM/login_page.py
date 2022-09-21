
from library.excel_library import read_locators
from library.config import Config
locators = read_locators(Config.LOCATORS_FILE_PATH,Config.LOGIN_SHEET_NAME)


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    def enter_username(self,username):
        user_loc = locators["username_txt"]
        self.driver.find_element(*user_loc).send_keys(username)

    def enter_password(self,password):
        pwd_loc = locators["password_txt"]
        self.driver.find_element(*pwd_loc).send_keys(password)

    def click_login(self):
        login_loc = locators["login_btn"]
        self.driver.find_element(*login_loc).click()

