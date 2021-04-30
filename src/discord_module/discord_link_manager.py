from selenium import webdriver

from src.models.discord_link import DiscordLink


class DiscordLinkManager:

    def __init__(self):
        self.message_list = []

    # TODO: There might be a bug when multiple new messages needs to be processed at the same time
    def update_messages(self, messages):
        for msg in messages:

            datetime = msg.find_element_by_xpath("//h2[@class='header-23xsNx']/span[2]/time").get_attribute("datetime")
            body = msg.find_element_by_xpath("//div[@class='grid-1nZz7S']/div[2]/a")
            link = body.get_attribute("href")
            description = body.text
            dl = DiscordLink(datetime, link, description)
            self.message_list.append(dl)
            if len(self.message_list) == 0 or self.message_list[-1].datetime < dl.datetime:

                self._check_sku(dl)

    def _check_sku(self, discord_link):
        print(len(self.message_list))
        driver = webdriver.Firefox()
        driver.get(discord_link.link)
        if discord_link.description.find("RTX 3070") != -1 or discord_link.description.find("RTX 3080") != -1:
            driver.get_screenshot_as_file(str(discord_link.datetime.timestamp()) + ".png")
            print(discord_link.link)
