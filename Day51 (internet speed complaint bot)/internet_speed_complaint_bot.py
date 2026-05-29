import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options



chrome_driver_path= r"C:\development\chromedriver-win64\chromedriver.exe"
service= Service(chrome_driver_path)
options= Options()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(service= service, options=options)

PROMISED_DOWN= 150
PROMISED_UP= 20
TWITTER_EMAIL = "00000000000000"
TWITTER_PASSWORD = "00000000000000000000"


class InternetSpeedTwitterBot:
    def __init__(self):
        global driver
        self.driver = driver
        self.down = 0
        self.up = 0

    # def get_internet_speed(self):
    #     self.driver.get("http://puspfc.speedtestcustom.com/")
    #     sleep(20)
    #
    #
    #     go_button = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/button')
    #     go_button.click()
    #     sleep(50)
    #
    #     self.down = float(self.driver.find_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[2]/div[1]/div[2]/div[1]/div/span').text)
    #     self.up = float(self.driver.find_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[2]/div[2]/div[2]/div[1]/div/span').text)
    #     print(self.down, self.up)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")

        time.sleep(20)
        email = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
        email.click()

        email.send_keys(TWITTER_EMAIL)
        time.sleep(10)
        password = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)

        password.send_keys(Keys.ENTER)

        time.sleep(30)
        tweet_compose = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
#bot.get_internet_speed()
bot.tweet_at_provider()
