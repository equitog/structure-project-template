from util_class.module_config import ConfigJson
import sqlalchemy
from os import path
from pandas import DataFrame
from util_class.mail import Mail
from util_class.module_html import Html


def insert(data: DataFrame, msg_boolean: bool, id_database: int, id_table: int):
    """
    msg_boolean
    :param id_table:
    :param data:
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

    string_connect_engine = "mssql+pyodbc://%s:%s@%s:1433/%s?driver=%s" % (user,
                                                                           password,
                                                                           host,
                                                                           name,
                                                                           driver)
    try:
        engine = sqlalchemy.create_engine(string_connect_engine, pool_size=0, max_overflow=-1)

        if msg_boolean:
            print('INFO: Process of insert start')
            data.to_sql(table_name, engine, schema=schema, if_exists='append', chunksize=50, index=False)

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
