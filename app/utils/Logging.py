import datetime


class Static_Log:
    '''
    This class should not be open to all developers.
    '''
    requested_path: str = None
    client_ip: str = None
    __log_file = None
    __instance = None
    
    @staticmethod
    def get_instance(requested_path: str, client_ip: str):
        if Static_Log.__instance:
            return Static_Log.__instance(requested_path, client_ip)
        else:

            raise Exception("No instance was made.")
            
    def __init__(self, requested_path: str, client_ip: str) -> None:
        self.requested_path = requested_path
        self.client_ip = client_ip
        self.__log_file = None
        if Static_Log.__instance:
            raise Exception("Cannot make another instance of Static_Log.")
        else:
            Static_Log.__instance = self #Safe to set it now
            time_format = '%d-%b-%Y'
            file_name = datetime.now().strftime(time_format)
            with open('logs/{}.txt'.format(file_name), mode='a+') as self.__log_file:
                date_time_message = datetime.now().strftime(f'{time_format}, %H:%M:%S | ')
                message = date_time_message + requested_path + ' | ' + client_ip + '\n'
                self.__log_file.write(message)
    