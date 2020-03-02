import json
import os
import time
from math import ceil

from newsapi import NewsApiClient

import chisquaredmodel


class GoogleNews:
    api = NewsApiClient(api_key="7e2115121651467cbc864d78fee56149")
    page_size = 100

    @classmethod
    def get_sources(cls):
        return cls.api.get_sources()

    @classmethod
    def get_articles_new(cls):
        return cls.api.get_top_headlines(page_size=cls.page_size)["articles"]

    @classmethod
    def get_articles_past(cls):
        # articles = []
        # for i in range(ceil(response["totalResults"] / cls.page_size)):
        #     response = cls.api.get_top_headlines(page_size=cls.page_size, page=(i + 1))
        #     articles.extend(response["articles"])
        #     print(len(articles))
        return cls.api.get_everything(language="en", page_size=cls.page_size, domains="techcrunch.com, engadget.com")["articles"]

    @classmethod
    def data_dump(cls):
        data = {}
        response = cls.api.get_top_headlines(page_size=cls.page_size)
        # articles = []
        # for i in range(ceil(response["totalResults"] / cls.page_size)):
        #     response = cls.api.get_top_headlines(page_size=cls.page_size, page=(i + 1))
        #     articles.extend(response["articles"])
        #     print(len(articles))
        for article in response["articles"]:
            if article["content"] is not None:
                data[article["url"]] = article["content"]
        if not os.path.exists("data/news/"):
            os.makedirs("data/news/")
        with open("data/news/articles.json", "w") as file:
            json.dump(data, file)


if __name__ == '__main__':
    for i in range(8):
        data = GoogleNews.get_articles_new()
        for article in data:
            if article["content"] is not None:
                chisquaredmodel.add_article(article["url"], article["content"])
        time.sleep(900)
