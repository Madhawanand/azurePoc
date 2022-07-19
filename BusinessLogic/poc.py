import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
class TestPoc:

    def test_invoke(self):
     self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     self.driver.get("https://www.youtube.com/")
     self.driver.maximize_window()
     self.driver.implicitly_wait(30)
     self.driver.find_element(By.XPATH ,"//input[@id='search']").send_keys("Paramatma")
     self.driver.close()
