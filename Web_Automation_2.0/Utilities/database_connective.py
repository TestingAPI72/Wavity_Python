from sqlite3.dbapi2 import *
import sqlite3
from Utilities.logger_log import customLogger

log = customLogger()


class database_connective:

    def __init__(self):
        self.dbname = 'Wavity_users_data.db'
        self.create_data_base = sqlite3.connect(self.dbname)
        self.connect_to_data_base = None

    def accessing_database(self, values='credientals'):
        global user_data
        self.connect_to_data_base = self.create_data_base.cursor()
        try:
            if not self.is_table():
                self.connect_to_data_base.execute("""CREATE TABLE Users (Email text, Password text)""")
        except OperationalError:
            log.error("Table already Exists")
        self.connect_to_data_base.execute("""INSERT INTO Users VALUES('suryap@wavity.com','Tenant@2')""")
        if values == 'credientals':
            user_data = []
            self.connect_to_data_base.execute("""SELECT Email FROM Users""")
            self.create_data_base.commit()
            username = self.connect_to_data_base.fetchall()
            if username:
                user_data.append(username[0][0])
            else:
                raise Exception("Username doesn't exists")
            self.connect_to_data_base.execute("""SELECT Password FROM Users""")
            self.create_data_base.commit()
            password = self.connect_to_data_base.fetchall()
            if password:
                user_data.append(password[0][0])
            else:
                raise Exception("Password doesn't exists")
            self.connect_to_data_base.execute("""DROP TABLE Users""")
            self.create_data_base.commit()
        return user_data

    def is_table(self, table_name='Users'):
        query = "SELECT name from sqlite_master WHERE type='table' AND name='{" + table_name + "}';"
        cursor = self.connect_to_data_base.execute(query)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True

    def data_base_teardown(self):
        try:
            self.create_data_base.close()
        except:
            log.error("can't able to close the database connection")

if __name__ == '__main__':
    d1 = database_connective()
    print(d1.accessing_database())
