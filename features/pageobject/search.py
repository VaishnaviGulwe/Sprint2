import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SEARCH(BaseSettingsPage):
    def __int__(self,driver):
        super().__init__(driver)
    def text_Searchbar(self, searchTEXT):
        time.sleep(3)
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.XPATH,ConfigReader("locators","SEARCHBAR_XPATH"))))

        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH", searchTEXT)


    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_XPATH")
