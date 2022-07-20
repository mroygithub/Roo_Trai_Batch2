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
        driver.get(Common.resdXMLAsPerNode("applicationURL_cub"))
        driver.implicitly_wait(10)


        # Click on Learn Cuber Basic ..

        driver.find_element(By.XPATH, cuberPage.learncuberbasic()).click()
        driver.implicitly_wait(10)
        print(driver.title)
        driver.back()
        time.sleep(5)

        # click on Twitter Link

        ele = driver.find_element(By.XPATH, cuberPage.footergitBTN())
        driver.execute_script("arguments[0].scrollIntoView();" , ele)
        ele.is_displayed
        #driver.execute_script("arguments[0].click();",ele)
        ele.click()
        #ele.click
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])

        # Do Some Activity in Child Window ...& Print the Title ..

        print(driver.title)


        driver.close
        time.sleep(5)
        # Switch To Parent Window ...

        driver.switch_to.window(driver.window_handles[0])

        print(driver.title)

        # Do Some Testing ...


        driver.quit

obj = TestLocators()
obj.IdentifyLocators()



