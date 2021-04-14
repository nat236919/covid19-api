# Here you can find all of the developing or approved vaccines in every phase. You can sort the table based on each
# columns or search for a unique vaccine name.
from typing import Any
import requests


class vaccine_abstraction:

    def __init__(self, imp):
        self._imp = imp

    def get_vaccine_data(self) -> Any:
        return self._imp.get_vaccine_data()


class vaccine_implementor:
    """ Model and Its methods """
    __instance = None

    @staticmethod
    def getInstance():
        if vaccine_implementor.__instance is None:
            """creating single instance """
            vaccine_implementor()
            return vaccine_implementor.__instance

    def __init__(self):
        self.url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-all-treatment"
        self.headers = {
            'x-rapidapi-key': "770aeab636msh7d96b4b6f420dc6p19b93ejsnefbca91bf4fa",
            'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

    def get_vaccine_data(self):
        try:
            response = requests.request("GET", self.url, headers=self.headers)
            # Get the list of the json object, but since the api only get the single object at a time, can get it
            # with the name of developerResearcher
            return response.json()
        except Exception as e:
            return e


class vaccine:
    """
    vaccine_implementor : Concrete Implementor
    vaccine_abstraction : Abstraction's Interface
    """

    def __init__(self):
        self.v = vaccine_implementor()
        self.v_abs = vaccine_abstraction(self.v)

    def get_vaccine_data(self):
        return self.v_abs.get_vaccine_data()
