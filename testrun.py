import json

import twitterhandler
from textcleaner import TextCleaner
from emotionanalyzer import EmotionAnalyzer
from nltk.corpus import gutenberg


def main():
    # tweets = twitterhandler.get_tweets(refresh=True, num_tweets=1)
    # clean = TextCleaner.letters(tweets)
    # refined = TextCleaner.exclude(clean)
    refined = TextCleaner.exclude(gutenberg.words('carroll-alice.txt'))
    # with open("data/words.json", "r") as file:
    #     refined = json.load(file)
    example_1 = EmotionAnalyzer("alice", refined)
    example_1.analyze()
    example_1.print_data()


if __name__ == "__main__":
    main()
