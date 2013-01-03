import psycopg2
from ..settings import *

class DatabaseHelper():
    """docstring for DatabaseHelper"""

    def __init__(self):
        self.connection = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)
        self.cursor = self.connection.cursor()

    def create_table(self, tableName):
        """
        Drops existing one if present
        """
        self.execute("DROP TABLE IF EXISTS " + tableName + ";")
        self.execute("CREATE TABLE " + tableName + " (id serial PRIMARY KEY, num integer, data varchar);")
        self.commit()

    def execute(self, sql):
        self.cursor.execute(sql)

    def execute_with_params(self, sql, params):
        """
        sql: "INSERT INTO test (num, data) VALUES (%s, %s)"
        params: (100, "abc'def")
        """
        self.cursor.execute(sql, params)

    def query(self, sql):
        cursor.execute(sql)
        return cursor.fetchone()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()