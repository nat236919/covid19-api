from typing import Any

import requests


class Target:

    def __init__(self):
        self._news = NewsUpdatesData()

    # Abstract Method
    def get_request(self):
        pass


class NewsAdapter(Target):

    def get_request(self):
        return self._news.get_news_updates_india()


class NewsUpdatesData:
    """ Model and Its methods """
    instance = None

    @staticmethod
    def getInstance():
        if NewsUpdatesData.instance is None:
            """here we are creating singleton instance """
            NewsUpdatesData()
            return NewsUpdatesData.instance

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


class news_updates:

    def __init__(self):
        self.newsAdapter = NewsAdapter()

    def get_news_updates_india(self):
        return self.newsAdapter.get_request()
