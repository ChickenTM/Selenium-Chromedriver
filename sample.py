from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest

class PythonOrg(unittest.TestCase):
    def setUp(self):
        Driver_Path = "\chromedriver\chromedriver.exe"
        serv = Service(Driver_Path)
        self.driver = webdriver.Chrome(service = serv)
    
    def test_search(self):
        driver = self.driver
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        self.assertIn("Web Form", driver.title)

        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
