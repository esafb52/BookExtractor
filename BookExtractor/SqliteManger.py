import sqlite3


class DbHelper:

    def __init__(self, db):
        self.db_name = db

    def __connect(self):
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except Exception as e:
            print('connection error!! ', e)

    def run_cmd(self, cmd):
        try:
            conn = self.__connect()
            res = conn.execute(cmd)
            return res
        except Exception as e:
            print('cmd run error!! ', e)
