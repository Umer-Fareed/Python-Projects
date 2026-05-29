from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_driver_path= r"C:\development\chromedriver-win64\chromedriver.exe"
service= Service(chrome_driver_path)

option= Options()
option.add_experimental_option("detach" , True)

driver= webdriver.Chrome(service= service, options=option)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname= driver.find_element(By.NAME,"fName")
fname.send_keys("fareed")
lname= driver.find_element(By.NAME, "lName")
lname.send_keys("kamboh")
email= driver.find_element(By.NAME, "email")
email.send_keys("fareedkambho@gmail.com")

signup= driver.find_element(By.CSS_SELECTOR, "form button")
signup.click()