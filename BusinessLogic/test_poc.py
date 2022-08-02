import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service


class TestPoc:

    def test_invoke(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()
        self.driver.close()
