from xml.dom import minidom
from pathlib import Path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time



def resdXMLAsPerNode(your_test_param):

        first_parse_XML = minidom.parse(str(Path(__file__).parent.parent)+"/readData.xml")
        data = first_parse_XML.getElementsByTagName(your_test_param)[0]
        return data.firstChild.data

def mousehoverusingpython(driver,ele):
        a = ActionChains(driver)
        ele = driver.find_element(By.XPATH, ele)
        a.move_to_element(ele).perform()
        time.sleep(3)
