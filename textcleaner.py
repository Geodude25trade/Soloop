import re


class TextCleaner:

    @staticmethod
    def letters(text, replace=" "):
        return re.sub(r"[^a-zA-Z]+", replace, text)
