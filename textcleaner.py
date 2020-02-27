import re
import json


class TextCleaner:

    @staticmethod
    def letters(text, replace=" "):
        return re.sub(r"[^a-zA-Z]+", replace, text)

    @staticmethod
    def exclude(text):
        if isinstance(text, str):
            text = text.split(" ")
        with open('words.json') as json_file:
            words = json.load(json_file)
        trimmed = []
        for string in text:
            if string in words:
                trimmed.append(string)
        return trimmed
