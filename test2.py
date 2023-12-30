from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r'C:\Users\e408590\Desktop\project\Scrapy\Selenium\chromedriver\chromedriver.exe'

pxy = "172.24.175.125:9090"

chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s' % pxy)
driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)

#temp_variable = 
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#print("output:", type(temp_variable))