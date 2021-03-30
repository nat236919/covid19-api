from covid_api_v2_integrator import CovidAPIv2Integrator

class Factory:
    "The Factory Class"

    @staticmethod
    def select_version(version):
        "A static method to get a concrete product"
        if version == 'v2':
            return CovidAPIv2Integrator()
        return None