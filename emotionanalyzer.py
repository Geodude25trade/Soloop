import json
import os
from nrclexicon import NRCLexicon


class EmotionAnalyzer:
    data = {}

    def __init__(self, name, text):
        self.path = "data/artefacts/" + name + "/"
        self.filename = name + ".json"
        self.name = name
        self.data["text"] = text

    def analyze(self):
        self.data["emotions"] = {}
        for word in self.data["text"]:
            if word in NRCLexicon.data:
                for emotion in NRCLexicon.data[word]:
                    if emotion not in self.data["emotions"]:
                        self.data["emotions"][emotion] = NRCLexicon.data[word][emotion]
                    else:
                        self.data["emotions"][emotion] += NRCLexicon.data[word][emotion]
        self.__save__()

    def __save__(self):
        if not os.path.exists(f"{self.path}"):
            os.makedirs(self.path)
        with open(f"{self.path}{self.filename}", "w") as file:
            json.dump(self.data, file)

    def __load__(self):
        if os.path.exists(f"{self.path}{self.filename}"):
            with open(f"{self.path}{self.filename}", "r") as file:
                self.data = json.load(file)
