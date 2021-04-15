import logging
from datetime import datetime

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object, metaclass=Singleton):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("testt")
        self._logger.setLevel(logging.INFO)

        time_format = '%d-%b-%Y'
        file_name = datetime.now().strftime(time_format)
        logging.basicConfig(filename='logs/{}.txt'.format(file_name), format='%(asctime)s:%(message)s')

    def get_log(self):
        return self._logger


