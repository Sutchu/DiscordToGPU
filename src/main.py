import time

from discord_module.discord_client import DiscordMonitor
from discord_module.discord_link_manager import DiscordLinkManager

monitor = DiscordMonitor()

time.sleep(7)
monitor.click_server()
link_manager = DiscordLinkManager()

while True:
    items = monitor.read_message_list()
    link_manager.update_messages(items)
    time.sleep(0.1)