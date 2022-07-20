from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append("/Users/mithunroy/Desktop/SelPyBatch2")
from reusableT import Common
from PageObject import cuberPage
import time


class TestLocators:

    def IdentifyLocators(self):

        driver = webdriver.Chrome(Common.resdXMLAsPerNode("chromepath"))
        driver.get("https://docker.com")
        driver.maximize_window()
        driver.implicitly_wait(10)

                    

        Common.mousehoverusingpython(driver, "(//a[text()='Products'])[1]")
        driver.find_element(By.XPATH, "(//a[text()='Docker Personal'])[1]").click()
        driver.implicitly_wait(10)
        driver.back()
        driver.implicitly_wait(10)


        Common.mousehoverusingpython(driver, "(//a[text()='Developers'])[1]")
        driver.find_element(By.XPATH, "(//a[text()='Community'])[1]").click()
        driver.implicitly_wait(10)
        driver.back()
        driver.implicitly_wait(10)



        Common.mousehoverusingpython(driver, "(//a[text()='About Us'])[1]")
        driver.find_element(By.XPATH, "(//a[text()='Careers'])[1]").click()
        driver.implicitly_wait(10)
        driver.back()
        driver.implicitly_wait(10)
        


        driver.quit

obj = TestLocators()
obj.IdentifyLocators()



