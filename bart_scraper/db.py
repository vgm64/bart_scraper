""" DB interface.
"""
import MySQLdb
import sqlite3
import datetime


class BartDB(object):
    def __init__(self, user=None, pw=None, engine='MySQLdb', db='bart'):
        if engine == 'MySQLdb':
            self.db = MySQLdb.connect(host='localhost', user=user, pw=pw, db='bart')
            self.cursor = self.db.cursor()
        if engine == 'sqlite3':
            self.db = sqlite3.connect(database=db)
            self.cursor = self.db.cursor()
            try:
                self.cursor.execute("SELECT * FROM etd LIMIT 1")
            except sqlite3.OperationalError:
                self.cursor.execute("CREATE TABLE etd (time, data)")
                self.db.commit()

    def insert(self, timestamp, data):
        self.cursor.execute("""INSERT INTO etd (time, data) VALUES (?,?)""", (timestamp, repr(data)))
        self.db.commit()
