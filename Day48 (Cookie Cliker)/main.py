from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)

options = Options()
options.add_experimental_option("detach", True)  # 👈 keeps browser open

driver = webdriver.Chrome(service=service, options=options)

"""
driver.get("https://www.amazon.com/HAOYUYAN-Bluetooth-Headphones-Canceling-Waterproof/dp/B0FHK281GL/ref=sr_1_3?crid=3BF48YQ8KVM9Q&dib=eyJ2IjoiMSJ9.4sOIi-YwUbh1o106oU7qNd7u7JVq1NimYxsrBLxwGOrNCYfCMoqQ9OE8hpI_-2NvsmoRH068a3HB0q3x-Jk55JM98n1cA5VKUX9YzPNPcnLKVh0BD14z_i71-fO1up4St0kx2BlNbgCSC-Ch1T7FlxOxTaxQeB3d9Ed7Y_P_aKxjdETikIFJAqgHk8dob_AGzcxB4q-ZhywwRBn61EsNS8YqFACY68yhZod3J5oTL8c.ggI_AJ42-woUhs0MSst1pCr_VBjXwQ8dXWe5c8h2Gus&dib_tag=se&keywords=earbuds&qid=1756449603&sprefix=airbeds%2Caps%2C380&sr=8-3&th=1")
price_element = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
price = price_element.text

print("Price:", price)
"""

driver.get("https://www.python.org/")
"""
#find logo by name 
search_bar_element= driver.find_element(By.NAME, "q")
print(search_bar_element.tag_name)
print(search_bar_element.get_attribute("placeholder"))
"""

"""
#find element by class name 
logo= driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)
"""
"""
#find element by css selector
documentation_link= driver.find_element(By.CSS_SELECTOR,".documentation-widget a" )
print(documentation_link.text)
"""
"""
#find element by Xpath
find_bug= driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(find_bug.text)
"""
"""
#find multiple elements using css selector 
event_times= driver.find_elements(By.CSS_SELECTOR, ".event-widget time ")
event_names= driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events= {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
"""
