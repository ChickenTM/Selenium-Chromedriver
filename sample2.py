from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

Driver_Path = "\chromedriver\chromedriver.exe"
serv = Service(Driver_Path)

driver = webdriver.Chrome(service = serv)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
assert "Web form" in driver.title

elem = driver.find_element(By.XPATH, "//select[@name='my-select']")
all_options = elem.find_elements(By.TAG_NAME, "option")
for option in all_options:
    print("value: {} text: {}".format(option.get_attribute("value"), option.get_attribute("text")))
    option.click()
    time.sleep(3)
elem.click()
elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

time.sleep(10)
driver.close()