from MySQLdb import _mysql
import json


class Mariadb:
    host = ''
    name = ''
    user = ''
    password = ''

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password

    def connect(self):
        conn = _mysql.connect(host=self.host,
                              user=self.user,
                              password=self.password,
                              db=self.name)

        return conn

    def close(self):
        conn = self.connect()
        if conn:
            conn.close()
