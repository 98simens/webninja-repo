import sqlite3

class DB():
    def init(self):
        self.conn = sqlite3.connect("Main.db")
    def executeSelect(sql):
        cur = self.conn.cursor()    
        cur.execute(sql)
        data = cur.fetchone()               
        return data

    def executeSelectAll(self, sql):
        self.conn = sqlite3.connect("Main.db")
        cur = self.conn.cursor()    
        cur.execute(sql)
        data = cur.fetchall()               
        return data

    def executeCommand(self, sql):
        self.conn = sqlite3.connect("Main.db")
        cur = self.conn.cursor()    
        cur.execute(sql)
        data = cur.fetchall()
        self.conn.commit()               
