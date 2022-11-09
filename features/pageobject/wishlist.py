import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Wishlist(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)
    def ADD_TOWISHLIST(self):
        time.sleep(5)
        #CC = context.driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='path' and @class='eX72wL']")
        CC = self.driver.find_elements(By.CLASS_NAME,ConfigReader("locators","WISHLISTBUTTON_CLASSNAME"))
        AA = ActionChains(self.driver)
        AA.move_to_element(CC[0])
        AA.click(CC[0])
        AA.perform()
        time.sleep(5)

    def Check_product_in_wishlist(self):
        self.driver.refresh()
        time.sleep(5)
        self.ClickButton("WISHLISTPRODUCT_XPATH")
        time.sleep(2)

    def Delete_product_in_wishlist(self):
        CC = self.driver.find_elements(By.CLASS_NAME, ConfigReader("locators", "DELETEBUTTON_CLASSNAME"))
        CC[0].click()
        time.sleep(5)

    def Click_on_yes_remove(self):
        self.ClickButton("REMAOVEBUTTON_XPATH")
        time.sleep(4)





