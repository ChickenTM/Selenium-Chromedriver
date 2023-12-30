from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

Driver_Path = "\chromedriver\chromedriver.exe"
serv = Service(Driver_Path)

proxy = Proxy({
    'httpProxy' : 'http://172.24.175.125:9090',
    'httpsProxy' : 'http://172.24.175.125:9090',
})
options = webdriver.ChromeOptions()
options.proxy = proxy


driver = webdriver.Chrome(options = options, service = serv)

driver.get("https://www.google.co.in/")

search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys("amazon")
search.send_keys(Keys.RETURN)

search_result = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)
driver.Get
elements = driver.find_elements(By.PARTIAL_LINK_TEXT, "Amazon")
for element in elements[:5]:
    element.click()
    #element.click()
    #time.sleep(5)
    if "Amazon" not in driver.title:
        driver.back()
    else:
        break

time.sleep(3)

amazon_search = driver.find_element(By.ID, "twotabsearchtextbox")
amazon_search.clear()
amazon_search.send_keys("laptops")
amazon_search.send_keys(Keys.RETURN)

time.sleep(3)

'''for page_number in range(5):
    print("page no:", page_number)
    pagination = driver.find_element(By.CLASS_NAME, "s-pagination-item s-pagination-button" )
    pagination.click()
    time.sleep(3)'''

pages = driver.find_elements(By.CLASS_NAME, "s-pagination-item s-pagination-button" )
print("pagination found")
print(pages)

for page_number, page in enumerate(pages[:3]):
    print("page no", )
    page.click()
    time.sleep(3)

time.sleep(5)
