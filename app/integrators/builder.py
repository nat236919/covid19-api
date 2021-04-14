class DataBuilder:

    def __init__(self):
        self.data = CovidData()

    def set_confirmed(self, value):
        self.data.confirmed = value
        return self

    def set_death(self, value):
        self.data.death = value
        return self

    def set_recovered(self, value):
        self.data.recovered = value
        return self

    def get_result(self):
        return self.data


class CovidData:

    def __init__(self, confirmed=0, death=0, recovered=0):
        self.confirmed = confirmed
        self.death = death
        self.recovered = recovered
