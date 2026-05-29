import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options


chrome_driver_path= r"C:\development\chromedriver-win64\chromedriver.exe"
service= Service(chrome_driver_path)
options= Options()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(service= service, options=options)


SIMILAR_ACCOUNT = "ankit.ang"
USERNAME = "000000000000"
PASSWORD = "0000000"


class InstaFollower:
    def __init__(self):
        global driver
        self.driver = driver
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)

        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(10)
        password.send_keys(Keys.ENTER)
    def find_followers(self):
        time.sleep(10)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(6)
        followers = self.driver.find_element(By.XPATH, "//a[contains(@href,'/followers/')]")
        followers.click()

        time.sleep(6)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()