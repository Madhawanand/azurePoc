import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestPoc:

    def test_invoke(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()
        print(self.driver.current_url)
        self.driver.close()
