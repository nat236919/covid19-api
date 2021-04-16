from models.covid_api_v2_model import FormattedCountryModel

def readable(x):
    x = str(x)
    n = len(x)
    x = list(reversed(x))
    y = []
    for i in range(0, n, 3):
        y.extend(x[i:i+3])
        y.append(",")
    y = list(reversed(y))
    y = "".join(y).strip(",")
    return y

class Humanreadable:
    def __init__(self):
        pass

    def adapt(self, country):
        confirmed = readable(country.confirmed)
        deaths = readable(country.deaths)
        recovered = readable(country.recovered)
        active = readable(country.active)
        return FormattedCountryModel(
                location = country.location,
                confirmed = confirmed,
                deaths = deaths,
                recovered = recovered,
                active = active)

