from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


pxy = "172.24.175.125:9090"
chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s' % pxy)

driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

temp_variable = driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(15)
print("output:", type(temp_variable))
