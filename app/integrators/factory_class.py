from concrete_factory import ConcreteCovidAPIv1

class FactoryCovidAPIv1:
    "The Factory Class"

    @staticmethod
    def create_version(nameVersion):
        "Construct and return the final product"
        if nameVersion == "v1":
            return ConcreteCovidAPIv1()  
        return None
