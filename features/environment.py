from selenium import webdriver


def before_scenario(context,driver):

    browser_name = "chrome"

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


def after_scenario(context,driver):
    context.driver.quit()