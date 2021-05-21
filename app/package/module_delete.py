from os import path
import pyodbc
from module_config import ConfigJson
from module_html import Html
from mail import Mail


def delete_by_date(dates: tuple, msg_boolean: bool, id_database: int, id_table: int):
    """
    msg_boolean
    :param dates:
    :param id_table:
    :param msg_boolean:
    :param id_database:
    :return: Boolean
    """

    # 1. Set id database
    file_database = ConfigJson().get_content_json_date(file_json='db')["database"][id_database]
    host = file_database['HOST']
    name = file_database['NAME']
    user = file_database['USER']
    password = file_database['PASSWORD']
    driver = file_database['DRIVER']

    # 2. Set table
    file_table = ConfigJson().get_content_json_date(file_json='table')["table"][id_table]
    schema = file_table['SCHEMA']
    table_name = file_table['TABLE_NAME']
    delete_by = file_table['DELETE_BY']
    try:
        if msg_boolean:
            query_delete = "DELETE %s.%s WHERE %s >= ? AND %s <= ?" % (schema,
                                                                       table_name,
                                                                       delete_by,
                                                                       delete_by)

            connection_string = "DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (driver,
                                                                                     host,
                                                                                     name,
                                                                                     user,
                                                                                     password)

            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
            with cursor.execute(query_delete, (dates[0], dates[1])):
                print("INFO: Delete completed")
            con.close()
        return True
    except Exception as err:
        print("EXCEPTION: This exception cant continue.")
        # 01. Get the exceptions
        traceback_err = err.__traceback__
        class_error = err.__class__
        line_error = traceback_err.tb_lineno
        file_error = path.split(traceback_err.tb_frame.f_code.co_filename)[1]

        # 02. html
        html = Html(name_file='template_email_alert').get_html()
        html = html.format(class_error, err, file_error, line_error, 'json', 'url')

        # 03. Send email with the exception
        config_email = ConfigJson().get_content_json_date(file_json='mail')['mails'][0]
        mail = Mail(host=config_email['host'],
                    user=config_email['from'],
                    password=config_email['password'])
        mail.send_mail(from_mail=config_email['from'],
                       subject=config_email['subject'],
                       to=config_email['to'],
                       cc=config_email['cc'],
                       type_body='html',
                       body=html)
        return False


def truncate(msg_boolean: bool, id_database: int, id_table: int):
    """
    msg_boolean
    :param dates:
    :param id_table:
    :param msg_boolean:
    :param id_database:
    :return: Boolean
    """

    # 1. Set id database
    file_database = ConfigJson().get_content_json_date(file_json='db')["database"][id_database]
    host = file_database['HOST']
    name = file_database['NAME']
    user = file_database['USER']
    password = file_database['PASSWORD']
    driver = file_database['DRIVER']

    # 2. Set table
    file_table = ConfigJson().get_content_json_date(file_json='table')["table"][id_table]
    schema = file_table['SCHEMA']
    table_name = file_table['TABLE_NAME']
    try:
        if msg_boolean:
            query_delete = "TRUNCATE TABLE %s.%s" % (schema,
                                                     table_name)

            connection_string = "DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (driver,
                                                                                     host,
                                                                                     name,
                                                                                     user,
                                                                                     password)

            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
            with cursor.execute(query_delete):
                print("INFO: Truncate completed")
        return True
    except Exception as err:
        print("EXCEPTION: This exception cant continue.")
        # 01. Get the exceptions
        traceback_err = err.__traceback__
        class_error = err.__class__
        line_error = traceback_err.tb_lineno
        file_error = path.split(traceback_err.tb_frame.f_code.co_filename)[1]

        # 02. html
        html = Html(name_file='template_email_alert').get_html()
        html = html.format(class_error, err, file_error, line_error, 'json', 'url')

        # 03. Send email with the exception
        config_email = ConfigJson().get_content_json_date(file_json='mail')['mails'][0]
        mail = Mail(host=config_email['host'],
                    user=config_email['from'],
                    password=config_email['password'])
        mail.send_mail(from_mail=config_email['from'],
                       subject=config_email['subject'],
                       to=config_email['to'],
                       cc=config_email['cc'],
                       type_body='html',
                       body=html)
        return False
