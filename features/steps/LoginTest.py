import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.LoginPage import LoginPage


@given(u'provide valid username')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.username("standard_user")
    #context.driver.find_element(By.ID, "user-name").send_keys("standard_user")


@when(u'provide valid password')
def step_impl(context):
    context.login_page.password("secret_sauce")
    #context.driver.find_element(By.ID, "password").send_keys("secret_sauce")


@when(u'click login button')
def step_impl(context):
    context.login_page.click_login_btn()
    #context.driver.find_element(By.ID, "login-button").click()


@then(u'verify home page header text as swag labs')
def step_impl(context):
    time.sleep(3)
    #context.home_page = HomePage()

    assert "Swag Labs" == context.driver.find_element(By.XPATH, "//div[@class='app_logo']").text
