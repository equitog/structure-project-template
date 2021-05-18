from os import path
from datetime import datetime, timedelta
import json
import pytz


class ConfigJson(object):
    __root_dir = path.dirname(path.abspath(__name__))

    def get_content_json(self, file_json: str = 'date') -> dict:
        dir_json = self.__root_dir + f'\\config\\{file_json}.json'
        with open(dir_json, 'r') as json_file:
            j = json_file.read()
        str_to_dict = json.loads(j)
        return str_to_dict

    def get_database_credential(self, id_database: int) -> dict:
        credential: dict = self.get_content_json(file_json="db")["database"][id_database]
        return credential

    def get_table_info(self, id_table: int) -> dict:
        tables: dict = self.get_content_json(file_json="table")["tables"][id_table]
        return tables

    def get_sp_info(self, id_sp: int) -> dict:
        sp: dict = self.get_content_json(file_json="store_procedure")["procedures"][id_sp]
        return sp


# class Configuration(ConfigJson):
#     __data = ConfigJson().get_content_json(file_json='date')["date_config"]
#
#     def __init__(self, id_date: int = None, keyword: str = None):
#         if id_date is None:
#             raise Exception('You must use the "id_date" argument')
#         elif keyword is None:
#             raise Exception('You must use the "Keyword" argument')
#
#         self.__main = self.__data[id_date][keyword]
#
#     def get_date_iso8601(self, utc: bool = True) -> tuple:
#         """
#
#         :param utc: You can get the date UTC or local, when arg. utc = True is date UTC and utc = False is date local
#         :return: list
#         """
#
#         if len(self.__main) == 0 and utc:
#             # Date UTC
#             zone_utc = pytz.timezone("UTC")
#             date_string_ini = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')  # Date ini Peru
#             date_string_fin = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d 23:59:59')  # Date end Peru
#
#             date_string_ini = datetime.strptime(date_string_ini, "%Y-%m-%d %H:%M:%S")
#             date_string_fin = datetime.strptime(date_string_fin, "%Y-%m-%d %H:%M:%S")
#
#             start = date_string_ini.astimezone(zone_utc).strftime("%Y-%m-%dT05:00:00")
#             end = date_string_fin.astimezone(zone_utc).strftime("%Y-%m-%dT04:59:59")
#             self.__main.append(start)
#             self.__main.append(end)
#         elif len(self.__main) == 0 and utc is False:
#             start = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT00:00:00")
#             end = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT23:59:59")
#             self.__main.append(start)
#             self.__main.append(end)
#         elif len(self.__main) == 2 and utc:
#             # Date UTC
#             zone_utc = pytz.timezone("UTC")
#
#             date_string_ini = datetime.strptime(self.__main[0].replace("T", " "), "%Y-%m-%d %H:%M:%S")
#             date_string_fin = datetime.strptime(self.__main[1].replace("T", " "), "%Y-%m-%d %H:%M:%S")
#
#             start = date_string_ini.astimezone(zone_utc).strftime("%Y-%m-%dT%H:%M:%S")
#             end = date_string_fin.astimezone(zone_utc).strftime("%Y-%m-%dT%H:%M:%S")
#             self.__main = []
#             self.__main.append(start)
#             self.__main.append(end)
#
#         date_start = self.__main[0]
#         date_end = self.__main[1]
#
#         return date_start, date_end
#
#     def get_date_interval(self, interval: int, format_date: str) -> tuple:
#
#         if len(self.__main) == 0:
#             self.__main.append((datetime.now() - timedelta(minutes=interval)).strftime(format_date))
#             self.__main.append((datetime.now() - timedelta(minutes=interval)).strftime(format_date))
#
#         date_start = self.__main[0]
#         date_end = self.__main[1]
#
#         return date_start, date_end
