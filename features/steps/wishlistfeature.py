from behave import *
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from Utilities.configreader import ConfigReader
from features.pageobject.wishlist import Wishlist
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.pageobject.login import LOGIN
from features.pageobject.search import SEARCH
from features.pageobject.wishlist import Wishlist
from features.pageobject.profile import Profile

import time


#
#
# @given(u'We are on flipkart website')
# def step_impl(context):
#     context.driver.get("https://www.flipkart.com/")
#
#
# @when(u'Click login')
# def step_impl(context):
#     context.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a")
#
#
# @then(u'Enter your "{username}" in the feild')
# def step_impl(context,username):
#      context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys(username)
#
#
# @then(u'Enter your "{password}" in the box')
# def step_impl(context,password):
#      context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys(password)
#
#
#
# @then(u'Click login')
# def step_impl(context):
#      context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
#      time.sleep(5)
#
#
# @then(u'type "{searchTEXT}" in search bar')
# def step_impl(context,searchTEXT):
#     time.sleep(5)
#     WebDriverWait(context.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CLASS_NAME, "_3704LK")))
#     context.driver.find_element(By.CLASS_NAME,"_3704LK").click()
#     time.sleep(5)
#     WebDriverWait(context.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CLASS_NAME, "_3704LK")))
#     context.driver.find_element(By.CLASS_NAME,"_3704LK").send_keys(searchTEXT)
#
#
#
# @then(u'Click on search button')
# def step_impl(context):
#     time.sleep(5)
#     WebDriverWait(context.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
#     context.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
#
#
#
# @then(u'Click on the wishlist button')
# def step_impl(context):
#     #context.driver = webdriver.Chrome(ChromeDriverManager().install())
#     time.sleep(5)
#     #CC = context.driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='path' and @class='eX72wL']")
#     CC = context.driver.find_elements(By.CLASS_NAME, "eX72wL")
#     AA = ActionChains(context.driver)
#     AA.move_to_element(CC[0])
#     AA.click(CC[0])
#     AA.perform()
#     time.sleep(5)
#
#
#
# @then(u'Click on the username')
# def step_impl(context):
#     CC = ActionChains(context.driver)
#     CC.move_to_element(context.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div"))
#     CC.perform()
#
#
#
# @then(u'Click on the wishlist from the option listed')
# def step_impl(context):
#     time.sleep(5)
#     CC = ActionChains(context.driver)
#     CC.click(context.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul/li[5]/a"))
#     CC.perform()
#
#
#
# @then(u'Check the product is in the wishlist')
# def step_impl(context):
#     context.driver.refresh()
#     time.sleep(5)
#
# @then(u'Click on the wishlist product')
# def step_impl(context):
#     context.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[2]/a/div[2]/div[1]/div[1]").click()
#
#
# @then(u'Verify the product')
# def step_impl(context):
#     # context.driver = webdriver.Chrome(ChromeDriverManager().install())
#     time.sleep(7)
#
#
#
# @then(u'Close the tab')
# def step_impl(context):
#     #context.driver=webdriver.Chrome(ChromeDriverManager().install())
#     a = context.driver.window_handles[0]
#     w = context.driver.window_handles[1]
#     context.driver.switch_to.window(w)
#     time.sleep(3)
#     context.driver.close()
#     context.driver.switch_to.window(a)
#
#
#
# @then(u'Click on the delete button')
# def step_impl(context):
#     #context.driver.find_element(By.XPATH,"(//img[@class='_2Nq6Qc'])[1]").click()
#     r = context.driver.find_elements(By.CLASS_NAME, "_2Nq6Qc")
#     r[0].click()
#     time.sleep(7)
#     #raise NotImplementedError(u'STEP: Then Click on the delete button')
#
#
# @then(u'Click on the yes remove')
# def step_impl(context):
#     context.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[2]/a/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/button[2]").click()
#     time.sleep(6)
#
#
#
#
#
#
#
#
#
#
#
#
#
#



@given(u'We are on flipkart website')
def step_impl(context):
    context.login = LOGIN(context.driver)
    context.login.OpenPage()

@then(u'Enter your "{username}" in the feild')
def step_impl(context,username):
    context.login.Enter_Username(username)

@then(u'Enter your "{password}" in the box')
def step_impl(context,password):
    context.login.Enter_password(password)

@then(u'Click login')
def step_impl(context):
    context.login.Click_login()

@then(u'Type "{searchTEXT}" in search bar')
def step_impl(context,searchTEXT):
    context.search = SEARCH(context.driver)
    context.search.text_Searchbar(searchTEXT)

@then(u'Click on search button')
def step_impl(context):
    context.search.Click_SEARCHBUTTON()

@then(u'Click on the wishlist button')
def step_impl(context):
    context.wishlist = Wishlist(context.driver)
    context.wishlist.ADD_TOWISHLIST()

@then(u'Click on the username')
def step_impl(context):
    context.profile = Profile(context.driver)
    context.profile.hover_Profile()

@then(u'Click on the wishlist from the option listed')
def step_impl(context):
    context.profile.click_on_wishlist()

@then(u'Check the product is in the wishlist')
def step_impl(context):
    context.driver.refresh()


@then(u'Click on the wishlist product')
def step_impl(context):
    context.wishlist.Check_product_in_wishlist()

@then(u'Verify the product')
def step_impl(context):
    time.sleep(3)

@then(u'Close the tab')
def step_impl(context):
    context.profile.verify_PRODUCT()

@then(u'Click on the delete button')
def step_impl(context):
    context.wishlist.Delete_product_in_wishlist()

@then(u'Click on the yes remove')
def step_impl(context):
    context.wishlist.Click_on_yes_remove()



