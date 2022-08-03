import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestPoc:

    def test_invoke(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
    #    chrome_options.add_argument('--window-size=1420,1080')
    #    chrome_options.add_argument('--headless')
    #    chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()
        print(self.driver.current_url)
        self.driver.close()
