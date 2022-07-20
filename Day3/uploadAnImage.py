from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append("/Users/mithunroy/Desktop/SelPyBatch2")
from reusableT import Common
from PageObject import cuberPage
import time


class TestLocators:

    def IdentifyLocators(self):

        driver = webdriver.Chrome(Common.resdXMLAsPerNode("chromepath"))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.implicitly_wait(10)


        # Upload An Image ...
        #/Users/mithunroy/Desktop/aa.png

        driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys(Common.resdXMLAsPerNode("imagePath"))
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@value='Upload']").click()
        time.sleep(5)
        


        driver.quit

obj = TestLocators()
obj.IdentifyLocators()



