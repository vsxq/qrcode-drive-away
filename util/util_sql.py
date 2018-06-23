import sqlite3
from collections import namedtuple
record = namedtuple("nametuple", ["tel", "date", "ip"])


class util_sql(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.db = sqlite3.connect("database.db", check_same_thread=False)

    def insert(self, tel, date, ip):
        insert_sql = "insert into record(tel,date,ip)  values(?,?,?)"
        self.db.execute(insert_sql, (tel, date, ip))
        self.db.commit()

    def select(self, tel):
        tel = str(tel)
        cursor = self.db.execute(
            "select ip,date from record where tel='{}'".format(tel))
        values = cursor.fetchall()
        if len(values) == 0:
            return  None
        else:
            results = []
            for i in values:
                result = {}
                result["ip"] = i[0]
                result["date"] = i[1]

                results.append(result)
            
            return  results
