from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time


Driver_Path = "\chromedriver\chromedriver.exe"
serv = Service(Driver_Path)

driver = webdriver.Chrome(service = serv)

driver.get("https://www.techwithtim.net/")

search = driver.find_element(By.CLASS_NAME, "search-field")
search.send_keys("test")
search.send_keys(Keys.RETURN)

#time.sleep(10)

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
    driver.close()

#main = driver.find_element(By.ID, "main")




