class Singleton:
    __instance__ = None

    def __init__(self):
        """ Constructor.
       """
        if Singleton.__instance__ is None:
            Singleton.__instance__ = self
        else:
            raise Exception("You cannot create another SingletonGovt class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not Singleton.__instance__:
            Singleton()
        return Singleton.__instance__

