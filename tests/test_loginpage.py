import time
import pytest


from POM.login_page import LoginPage
from library.excel_library import read_test_data
path = r"../files/test_data.xlsx"

user_data = (read_test_data(path,"login_credentials"))
class TestLoginPage:
    @pytest.mark.parametrize("user_,pwd_",user_data)
    def test_login(self,driver_init,user_,pwd_):
        try:
            driver = driver_init
            driver.implicitly_wait(10)
            lp = LoginPage(driver)
            lp.enter_username(user_)
            time.sleep(1)
            lp.enter_password(pwd_)
            time.sleep(1)
            lp.click_login()
            time.sleep(1)
            title = driver.title
            assert title == "actiTIME - Enter Time-Track"
        except BaseException as error_msg:
            driver.save_screenshot(r"C:\Users\HAMLIN INTERIORS\PycharmProjects\pythonProject\New_framework\screenshorts\error.png")
            raise error_msg