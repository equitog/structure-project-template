from getpass import getuser
from socket import gethostname, gethostbyname


class Machine:
    """
    Esta clase permite obtener información de la máquina.
    """
    __hostname = gethostname()
    __ip = gethostbyname(__hostname)
    __user = getuser()
    __host = ""

    def get_user(self):
        return self.__user

    def get_hostname(self):
        return self.__hostname

    def get_ip(self):
        return self.__ip
