from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys


chrome_driver_path= r"C:\development\chromedriver-win64\chromedriver.exe"
service= Service(chrome_driver_path)

options= Options()
options.add_experimental_option("detach", True)


driver= webdriver.Chrome(service= service, options= options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")
"""
#to click on webpage using selenium 
voters= driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[1]/a')
voters.click()
"""

#click by using link text
#all_portals= driver.find_element(By.LINK_TEXT, "all portals")
#all_portals.click()

#find element by name
search = driver.find_element(By.CSS_SELECTOR, "input[name='search']")
search.send_keys("python")
search.send_keys(Keys.ENTER)