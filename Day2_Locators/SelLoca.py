from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestLocators:

    def IdentifyLocators(self):

        driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("https://www.google.com")


        driver.find_element(By.NAME , "q").send_keys("Robot Framework")
        time.sleep(10)

        # Do Some Testing ...


        driver.quit

obj = TestLocators()
obj.IdentifyLocators()



