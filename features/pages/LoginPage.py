from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def username(self, uname):
        self.driver.find_element(By.ID, "user-name").send_keys(uname)

    def password(self, pwd):
        self.driver.find_element(By.ID, "password").send_keys(pwd)

    def click_login_btn(self):
        self.driver.find_element(By.ID, "login-button").click()





