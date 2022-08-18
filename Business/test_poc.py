from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Business.BasePage import BaseTest


class TestPoc(BaseTest):

    def test_invoke(self):
        self.log=self.getLogger()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.log.info("Youtube got opened")
        self.driver.maximize_window()
        self.log.info("Window got maximised")
        url=self.driver.current_url
        self.log.info(url)
        self.driver.close()

    def test_search(self):
        self.log = self.getLogger()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//input[@id='search']").send_keys("paramatma")
        self.log.info("Paramatma has been searched")
        self.driver.close()
