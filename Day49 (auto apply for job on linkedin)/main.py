from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_driver_path= r"C:\development\chromedriver-win64\chromedriver.exe"
service= Service(chrome_driver_path)
options= Options()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(service= service, options=options)

driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4292742986")

EMAIL_ID = "YOUR MAIL"
PASSWORD = "YOUR PASSWORD"
PHONE = "1234567891"


driver_path = Service("DRIVER_PATH/chromedriver")
# create a driver obect for chrome
driver = webdriver.Chrome(service=driver_path)


# loading the linkedin page using driver
driver.get(URL)
driver.maximize_window()

# clicks on sign in button
sign_in_page = driver.find_element(By.CSS_SELECTOR, "div .nav__button-secondary").click()

# sleeping for 3 sec so that till than the signin page will load without showing any errors
time.sleep(3)

# inserting email and password
mail = driver.find_element(By.ID, "username")
mail.send_keys(EMAIL_ID)
password = driver.find_element(By.ID, 'password')
password.send_keys(PASSWORD)
click_sign_in = driver.find_element(By.CSS_SELECTOR, "div .from__button--floating").click()
# another method of clicking sign in  is by just pressing enter after entering password as shown below :
# password.send_keys(Keys.ENTER)

# sleeping for 3 sec so that till than the next page will load without showing any errors
time.sleep(5)

# click on first job on the page
click__first_job = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results__list li").click()


# additional way but I don't prefer this one
# ----------------------------------
# click__first_job = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list li div")
# last_element = []
# for item in click__first_job:
#     last_element.append(item)
#     if item.get_attribute('data-job-id') == "2914739894":
#         break
# last_element[-1].click()
# ------------------------------------

# click on easy apply
click_easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button").click()
add_number = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting'
                                           ':2914739616,43805565,phoneNumber~nationalNumber)"]')
# add phone number only if the field is empty, otherwise the no. field would have been auto completed by Linkedin
if add_number.get_attribute("value") == "":
    add_number.send_keys(PHONE)
# after adding number than click next and next
click_next = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end button').click()
resume_next = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()


# ------- english proficiency drop down--------
drop_box = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:'
                                      '2914739616,43805589,multipleChoice)')
# select drop down menu
english_drop = Select(drop_box)
# select option from drop down menu (using select by index) it's our own choice
english_drop.select_by_index(2)


# --------work experience drop down--------
next_drop_box = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized'
                                           '_jobPosting:2914739616,43805581,multipleChoice)')

experience_box = Select(next_drop_box)
# select option from drop down menu (using select by Visible text) it's our own choice
experience_box.select_by_visible_text('Yes')
click_review = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()

# click on submit------Your application will be submitted
click_submit = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()
