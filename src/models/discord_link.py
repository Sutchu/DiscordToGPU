import datetime as dt
class DiscordLink:
    def __init__(self, datetime, link, description):
        self.datetime = self._datetime_from_string(datetime)
        self.description = description
        self.link = link

    def _datetime_from_string(self, datetime):
        datetime = dt.datetime.strptime(datetime, "%Y-%m-%dT%H:%M:%S.%fZ")
        return datetime
