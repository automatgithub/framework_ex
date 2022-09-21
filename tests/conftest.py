
import pytest
from selenium import webdriver
from library.config import Config


@pytest.fixture()
def driver_init():
     if Config.BROWSER_NAME == "chrome":
          driver = webdriver.Chrome(executable_path=Config.CHROMEDRIVER_PATH)
     elif Config.BROWSER_NAME == "firefox":
          driver = webdriver.Firefox(executable_path=Config.GECKODRIVER_PATH)
     else:
          driver = webdriver.Edge(executable_path=Config.EDGEDRIVER_PATH)

     driver.get(Config.URL)
     driver.maximize_window()
     yield driver
     driver.close()