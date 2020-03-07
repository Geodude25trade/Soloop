import json
import os
import time
import datetime
import requests
from math import ceil


# import chisquaredmodel


class Guardian:
    api_key = ""
    url = "https://content.guardianapis.com/"

    def __init__(self, api_key="5046ff4b-1de1-4cd7-ba17-ace15f3e94ed"):
        self.api_key = api_key
        self.settings = {"api-key": api_key}
        self.articles = []
        self.tries = 0

    def add_setting(self, key, value):
        self.settings[key] = value

    def search(self):
        return requests.get(self.url + "search", self.settings)

    def search_full(self):
        year = datetime.datetime.now().year
        for y in range(2000, year):
            for m in range(1, 13):
                self.add_setting("from-date", f"{y}-{str(m).zfill(2)}-02")
                if m == 12:
                    self.add_setting("to-date", f"{y + 1}-01-01")
                else:
                    self.add_setting("to-date", f"{y}-{str(m + 1).zfill(2)}-01")
                print(f"\n{self.settings['from-date']} <--> {self.settings['to-date']}")
                self.add_setting("page", 1)
                pages = self.__get_articles()
                print(f"starting at page 1 of {pages} pages...")
                time.sleep(17.28)
                for i in range(2, pages + 1):
                    print(f"page {i}...")
                    self.add_setting("page", i)
                    self.__get_articles()
                    time.sleep(17.28)
        with open("data/news/articles.json", "w") as file:
            json.dump(self.articles, file)

    def __get_articles(self):
        results = self.search()
        if results.status_code == 200:
            self.tries = 0
            data = results.json()['response']
            self.articles.append(data['results'])
            return data['pages']
        elif self.tries < 5:
            self.tries += 1
            print("sleeping for two minutes")
            time.sleep(120)
            self.__get_articles()
        else:
            raise ConnectionError


if __name__ == '__main__':
    news = Guardian()
    news.add_setting("show-fields", "bodyText")
    news.add_setting("page-size", 200)
    news.add_setting("order-by", "oldest")
    news.add_setting("type", "article")
    news.search_full()
    # print(news.search())
