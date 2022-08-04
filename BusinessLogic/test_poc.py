import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPoc:

    def test_invoke(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()
        print(self.driver.current_url)

    def test_search(self):
        self.driver.find_element(By.XPATH, "//input[@id='search']").send_keys("paramatma")
        self.driver.close()
