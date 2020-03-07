import json
from collections import OrderedDict

import chisquaredmodel
from googlenews import GoogleNews
import twitterhandler
from textcleaner import TextCleaner
from emotionanalyzer import EmotionAnalyzer
from nltk.corpus import gutenberg


def main():
    # tweets = twitterhandler.get_tweets(refresh=True, num_tweets=5, track=["coronavirus", "hospital", "skateboarding"])
    # clean = TextCleaner.letters(tweets)
    # refined = TextCleaner.exclude(clean)
    # # refined = TextCleaner.exclude(gutenberg.words('carroll-alice.txt'))
    # # with open("data/words.json", "r") as file:
    # #     refined = json.load(file)
    # example_1 = EmotionAnalyzer("news", refined)
    # example_1.analyze()
    # example_1.print_data()
    data = GoogleNews.get_articles_new()
    for article in data:
        if article["content"] is not None:
            chisquaredmodel.add_article(article["url"], article["content"])
        break
    chisquaredmodel.compute_table_total()
    words = chisquaredmodel.calculate_article(data[0]["url"], data[0]["content"])
    sorted_data = OrderedDict(sorted(words.items(), key=lambda x: x[1], reverse=True))
    print(f"Title: {data[0]['title']}")
    print(f"Description: {data[0]['content']}\n")
    for name in sorted_data:
        print(f"{name}: {sorted_data[name]}")

    print("\n")
    tracker = ""
    for i in sorted_data:
        tracker = i
        break
    tweets = twitterhandler.get_tweets(refresh=True, num_tweets=100, track=[f"{tracker}"])
    clean = TextCleaner.letters(tweets)
    refined = TextCleaner.exclude(clean)
    example_1 = EmotionAnalyzer("news", refined)
    example_1.analyze()
    example_1.print_data()


if __name__ == "__main__":
    main()
