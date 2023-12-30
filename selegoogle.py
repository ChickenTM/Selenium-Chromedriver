from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time


# Driver_Path = "\chromedriver\chromedriver.exe"
# serv = Service(Driver_Path)

# driver = webdriver.Chrome(service = serv)
driver = webdriver.Chrome(
    r"C:\Users\mithun\Desktop\project\Scrapy\Selenium\chromedriver\chromedriver.exe"
)

driver.get("https://www.google.com/")

search = driver.find_element(By.NAME, "q")
search.send_keys("amazon")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    elems = driver.find_elements(By.PARTIAL_LINK_TEXT, "Amazon")
    for elem in elems:
        elem.click()
        if elem.title == "Amazon":
            break
        else:
            elem.back()
except:
    print("not found")

time.sleep(10)
"""
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME, "article")
    for enum, article in enumerate(articles):
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        print("article :", enum)
        print(header.text)
finally:
    driver.close()"""

# main = driver.find_element(By.ID, "main")
