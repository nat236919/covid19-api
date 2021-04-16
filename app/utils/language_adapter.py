from googletrans import Translator


class CountriesName:
    def name(self): pass


"""Adaptee"""


class NonEnglish:
    def name(self):
        return self


class Translator:

    def __init__(self, name):
        self.__name = name

    def translate(self):
        translator = Translator()
        text = self.__name
        result = translator.translate(text, dest='en')
        return result
