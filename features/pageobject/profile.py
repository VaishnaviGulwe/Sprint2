import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Profile(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)
    def hover_Profile(self):
        CC = ActionChains(self.driver)
        CC.move_to_element(self.driver.find_element(By.XPATH,ConfigReader("locators","PROFILE_XPATH")))
        CC.perform()

    def click_on_wishlist(self):
        time.sleep(5)
        CC = ActionChains(self.driver)
        CC.click(self.driver.find_element(By.XPATH, ConfigReader("locators","OPTIONLISTED_XPATH")))
        CC.perform()


    def verify_PRODUCT(self):

        BS = self.driver.window_handles[0]
        SS = self.driver.window_handles[1]
        self.driver.switch_to.window(SS)
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(BS)


