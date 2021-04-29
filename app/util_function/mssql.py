import pandas as pd
import pyodbc


def get_con(host: str, name: str, user: str, password: str, driver: str = 'ODBC Driver 13 for SQL Server'):
    string = "DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (driver,
                                                                  host,
                                                                  name,
                                                                  user,
                                                                  password)
    con = pyodbc.connect(string)

    return con


def read_sql(host, name, user, password, script) -> list:
    con = get_con(host=host, name=name, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(script)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


def update_sql(host, name, user, password, script):
    con = get_con(host=host, name=name, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(script)
    cursor.commit()
    cursor.close()
    con.close()
    return True


def insert_sql(host, name, user, password, script):
    con = get_con(host=host, name=name, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(script)
    cursor.commit()
    cursor.close()
    con.close()
    return True


def store_procedure_sql(host, name, user, password, script):
    try:
        con = get_con(host=host, name=name, user=user, password=password)
        cursor = con.cursor()
        cursor.execute(script)
        cursor.commit()
        cursor.close()
        con.close()
        return True, "", "", ""
    except Exception as err:
        # 01. Get the exceptions
        traceback_err = err.__traceback__
        class_error = str(err.__class__).replace("<class '", "").replace("'>", "")
        line_error = traceback_err.tb_lineno
        file_error = path.split(traceback_err.tb_frame.f_code.co_filename)[1]
        return False, class_error, line_error, file_error

