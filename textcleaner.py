import re


class TextCleaner:

    @staticmethod
    def letters(text, replace=" "):
        re.sub(r"[^a-zA-Z]+", replace, text)

    @staticmethod
    def numbers(text, replace=" "):
        re.sub(r"[^a-zA-Z]+", replace, text)
