from models.covid_api_v2_model import CountryModel

class CountryBuilder:
	def __init__(self):
		pass
	def build(self, parts):
		return CountryModel(**parts)

