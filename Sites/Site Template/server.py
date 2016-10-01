import sqlite3
import cherrypy
from cherrypy.lib import auth_digest
import os, os.path
from mako.template import Template
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

attributes = {}
def UpdateData():
    global attributes
    attributes = {"titel":executeSelect("SELECT Content,ContentID FROM Data WHERE ContentID = 1 AND PageID = 1"),
                  "Content":executeSelect("SELECT Content,ContentID FROM Data WHERE ContentID = 2 AND PageID = 1"),
                  "currentTheme":executeSelect("SELECT Content, ContentID from Data WHERE ContentID = 3 AND PageID = 1"),
                  "Themes":executeSelect("SELECT Content, ContentID from Data WHERE ContentID = 4 AND PageID = 1")}
UpdateData()

class Website(object):
    @cherrypy.expose
    def index(self):
        return Template(open("index.html").read().encode("cp1252","ignore")).render(attributes = attributes)
    @cherrypy.expose
    def edit(self):
        editContent = executeSelectAll("SELECT Content, ContentID, Name, Type from Data WHERE PageID = 1")
        return Template(open('edit.html').read().encode("cp1252","ignore")).render(attributes = editContent)
    @cherrypy.expose
    def EditContent(self, content, contentID):
        executeCommand("UPDATE Data SET Content = '" + str(content) + "' WHERE ContentID = " + str(contentID) + ";")
        UpdateData()
        raise cherrypy.HTTPRedirect("/edit")
        
        
if __name__ == '__main__':
    conf = {'/': {'tools.staticdir.on': True,'tools.staticdir.dir':'./','tools.mako.directories':"./", 'tools.staticdir.root': os.path.abspath(os.getcwd()),
                  'tools.encode.on': True,'tools.encode.encoding': 'utf-8','tools.staticfile.filename':"favicon.ico"},
    "global":{'server.socket_host': 'localhost',
                        'server.socket_port': 80,#executeSelect("SELECT port FROM Conf")[0]
                       }}
    cherrypy.Application(Website(), conf)
