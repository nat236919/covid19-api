from typing import Any

import requests


class news_updates:
    """ Model and Its methods """
    instance = None

    @staticmethod
    def getInstance():
        if news_updates.instance is None:
            """here we are creating singleton instance """
            news_updates()
            return news_updates.instance

    def __init__(self):
        self.url = "https://covid-19-india2.p.rapidapi.com/latest.php"
        self.headers = {
            'x-rapidapi-key': "64c524732fmshd3fcb40147d3b4bp1ce897jsn83f4f7602433",
            'x-rapidapi-host': "covid-19-india2.p.rapidapi.com"
        }

    def get_news_updates_india(self) -> Any:
        try:
            response = requests.request("GET", self.url, headers=self.headers)
            return response.json()
        except Exception as E:
            return E


i = news_updates()
print(i.get_news_updates_india())
