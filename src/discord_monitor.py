import time

from selenium import webdriver
import selenium.webdriver.common.keys as keys


class DiscordMonitor:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://discord.com/login")
        self.login("alisutchu@gmail.com", "sifre")

    # Enters username and password then presses login button
    def login(self, username, password):
        # Find useername, password fields and login button
        username_field = self.driver.find_element_by_name('email')
        password_field = self.driver.find_element_by_name('password')
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')

        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click login
        login_button.click()

    def click_server(self):
        ser_button = self.driver.find_element_by_xpath("//div[@data-list-item-id='guildsnav___822668443286372422']")
        ser_button.click()

        self.click_channel()

    def click_channel(self, recursive_counter=100):
        if recursive_counter == 0:
            print("Couldn't find the channel")
            return -1

        channels = self.driver.find_element_by_xpath("//div[@id='channels']")

        try:
            channel_button = self.driver.find_element_by_xpath(
                "//a[@data-list-item-id='channels___823213645507985438']")
            channel_button.click()
        except:
            time.sleep(2)
            # channels.send_keys(keys.Keys.UP)
            self.click_channel(recursive_counter - 1)

        return 0

    def read_message_list(self):
        mess = self.driver.find_element_by_xpath("//div[@aria-label='Messages in amazon']")
        for _ in range(10):
            mess.send_keys(keys.Keys.PAGE_DOWN)

        items = mess.find_elements_by_xpath("//div[@role='listitem']")
        return items
