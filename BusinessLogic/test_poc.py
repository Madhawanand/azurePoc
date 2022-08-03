import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestPoc:

    def test_invoke(self):
        options = webdriver.ChromeOptions()
    #    options.add_argument('headless')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--remote-debugging-port=9222')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()
        print(self.driver.current_url)
        self.driver.close()
