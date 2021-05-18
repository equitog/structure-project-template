from ldap3 import Server, Connection, ALL
import re
import json


def write_disable(string: str):
    with open("user_disabled.txt", "a+") as file:
        file.write(string + "\n")


server = Server("allus.pe", get_info=ALL)
conn = Connection(server=server, user="Meucci", password="sYnC4D.m3uCC1")
conn.bind()
try:
    allus_pe = open("allus.pe-emp_email.csv", "r", encoding="utf8")
    data = allus_pe.readlines()
    allus_pe.close()
    conn.search("DC=allus,DC=pe", f"(cn=Ernesto Edgar Quito Gonzales)", attributes=['userAccountControl', 'mail'])
    if len(conn.entries) > 0:
        for entry in conn.entries:
            dict_ = json.loads(entry.entry_to_json())
            print(dict_)

    # found = 0
    # not_found = 0
    #
    # for i in data:
    #     full_name, email, domain, user = i.split(";")
    #     full_name = full_name.replace("(*)", "")
    #     user = user.replace("\n", "")
    #
    #     # cn = 'ROSA ANGELI ASCURRA AVILA'
    #     conn.search("DC=allus,DC=pe", f"(cn={full_name})", attributes=['userAccountControl', 'mail'])
    #
    #     if len(conn.entries) > 0:
    #         found += 1
    #         for entry in conn.entries:
    #             dict_ = json.loads(entry.entry_to_json())
    #             # print(dict_)
    #             string = f"{full_name};{user};{dict_['attributes']['mail']}"
    #             write_disable(string=string)
    #     else:
    #         not_found += 1
    #         conn.search("DC=allus,DC=pe", f"(sAMAccountName={user})", attributes=['userAccountControl', 'mail'])
    #         if len(conn.entries) > 0:
    #             for entry in conn.entries:
    #                 dict_ = json.loads(entry.entry_to_json())
    #                 string = f"{full_name};{user};{dict_['attributes']['mail']}"
    #                 write_disable(string=string)
    #
    # print(found)
    # print(not_found)
except Exception as ee:
    print("Error")
    print(ee, ee.__class__)
finally:
    conn.unbind()
    print("finished")
