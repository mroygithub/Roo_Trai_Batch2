from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append("/Users/mithunroy/Desktop/SelPyBatch2")
from reusableT import Common
from PageObject import cuberPage
import time


class TestLocators:

    def IdentifyLocators(self):

        driver = webdriver.Chrome(Common.resdXMLAsPerNode("chromepath"))
        driver.get("https://docker.io/")
        driver.implicitly_wait(10)

        # Print All Links....

        lnks = driver.find_elements(By.XPATH,("//a"))
        for lnk in lnks:
            #print(lnk.text)
            print(lnk.get_attribute('href'))
            #if lnk.text == "Designed for extensibility":
                #break

        a = ActionChains(driver)
        ele= driver.find_element(By.XPATH,"(//a[text()='Products'])[1]")
        a.move_to_element(ele).perform()

        time.sleep(10)
      
        


        driver.quit

obj = TestLocators()
obj.IdentifyLocators()



