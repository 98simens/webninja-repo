import cherrypy
from cherrypy.lib import auth_digest
import os, os.path
from mako.template import Template
import sys
import sqlite3

def executeSelect(sql):
    conn = sqlite3.connect("Main.db")
    cur = conn.cursor()    
    cur.execute(sql)
    data = cur.fetchone()               
    conn.close()
    return data

def executeSelectAll(sql):
    conn = sqlite3.connect("Main.db")
    cur = conn.cursor()    
    cur.execute(sql)
    data = cur.fetchall()               
    conn.close()
    return data

def executeCommand(sql):
    conn = sqlite3.connect("Main.db")
    cur = conn.cursor()    
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()               
    conn.close()


    


#.encode("cp1252","ignore")
class Website(object):
    @cherrypy.expose
    def index(self):
        attributes = {}
        Data = executeSelectAll("SELECT ContentID, Content FROM Data WHERE PageID = 0")
        for Item in Data:
            attributes[Item[0]] = Item[1]
        print(attributes)
        return Template(open('index.html').read()).render(attributes = attributes)
    @cherrypy.expose
    def edit(self):
        ContAttributes = []
        editAttributes = {}
        Data = executeSelectAll("SELECT ContentID, Content, TypeID, Name FROM Data WHERE PageID = 0")
        for Item in Data:
            ContAttributes.append((Item[0], Item[1], Item[2], Item[3]))
        DataEdit = executeSelectAll("SELECT TypeID, HTML from Types")
        for Edit in DataEdit:
            editAttributes[Edit[0]] = Edit[1]
        attributes = [ContAttributes,editAttributes]
        return Template(open('edit.html').read()).render(attributes = attributes)

    @cherrypy.expose
    def edit_cont(self, ContID, Value):
        executeCommand("UPDATE Data SET Content ='"+Value+"' WHERE ContentID = "+ str(ContID))
        raise cherrypy.HTTPRedirect("/edit")
        
        
        
if __name__ == '__main__':
    conf = {'/': {'tools.staticdir.on': True,'tools.staticdir.dir':'./','tools.mako.directories':"./", 'tools.staticdir.root': os.path.abspath(os.getcwd()),
                  'tools.encode.on': True,'tools.encode.encoding': 'utf-8','tools.staticfile.filename':"favicon.ico"},}
    cherrypy.config.update({'server.socket_host': 'localhost',
                        'server.socket_port': 80,
                       })
    cherrypy.quickstart(Website(),'/', conf)

