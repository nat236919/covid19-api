from integrators.covid_api_v1_integrator import CovidAPIv1
from integrators.covid_api_v2_integrator import CovidAPIv2Integrator

class ApiAdaptor:

    def __init__(self):
        self.a1 = CovidAPIv1()
        self.a2 = CovidAPIv2Integrator()

    def current(self, a):
        if self.a == 1:
            self.a1.get_current_status()
        if self.a == 2:
            self.a2.get_current()

    def countries(self, a):
        if self.a == 1:
            self.a1.get_affected_countries()
        if self.a == 2:
            self.a2.get_country()

    def total(self, a):
        if self.a == 1:
            self.a1.get_total()
        if self.a == 2:
            self.a2.get_total()
    
    def confirmed(self, a):
        if self.a == 1:
            self.a1.get_confirmed_cases()
        if self.a == 2:
            self.a2.get_confirmed()
    
    def recovered(self, a):
        if self.a == 1:
            self.a1.get_recovered()
        if self.a == 2:
            self.a2.get_recovered()
    
    def death(self, a):
        if self.a == 1:
            self.a1.get_deaths()
        if self.a == 2:
            self.a2.get_deaths()

        