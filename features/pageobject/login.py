import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LOGIN(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)
    def OpenPage(self):
        self.DynamicImplicitWait(40)
        self.driver.get(ConfigReader("base info","URL"))
    def Enter_Username(self,username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH",username)
    def Enter_password(self,password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("PASSWORD_XPATH", password)
    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_XPATH")