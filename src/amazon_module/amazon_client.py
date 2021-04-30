import time

from selenium.webdriver import Firefox

class AmazonClient:
    def __init__(self):
        self.driver = Firefox()
        self.driver.get("https://www.amazon.com/gp/product/B07CVPKD8Z")

    def click_buynow(self):
        buy_now_button = self.driver.find_element_by_xpath("//input[@id='buy-now-button']")
        buy_now_button.click()

new = AmazonClient()
new.click_buynow()

time.sleep(20)

buy = AmazonClient()
buy.click_buynow()