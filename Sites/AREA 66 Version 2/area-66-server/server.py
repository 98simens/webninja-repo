import sqlite3
import sql
import cherrypy
from cherrypy.lib import auth_digest
import os, os.path
from mako.template import Template

attributes = {}
database = sql.DB()
def UpdateData():
    global attributes
    data = database.executeSelectAll("SELECT ContentID, Content, Name from Data")
    for i in data:
        attributes[i[0]] = i[1]
    attributes["Images"] = database.executeSelectAll("SELECT ImgID, src, Version FROM Images ORDER BY ImgID")

def fix_str(string):
    string = string.replace(" ","_")
    string = string.replace("å","a")
    string = string.replace("ä","a")
    string = string.replace("ö","o")
    return string
    


class Website(object):
    @cherrypy.expose
    def index(self):
        return Template(open("index.html").read().encode("cp1252","ignore")).render(attributes = attributes)
    @cherrypy.expose
    def edit(self):
        editContent = database.executeSelectAll("SELECT Content, ContentID, Name, Type from Data WHERE PageID = 1")
        return Template(open('edit.html').read().encode("cp1252","ignore")).render(attributes = editContent)
    @cherrypy.expose
    def edit_img(self, f=None):
        editContent = database.executeSelectAll("SELECT ImgID, src, Version FROM Images ORDER BY ImgID")
        return Template(open('edit_img.html').read().encode("cp1252","ignore")).render(attributes = editContent)
    @cherrypy.expose
    def EditContent(self, content, contentID):
        database.executeCommand("UPDATE Data SET Content = '" + str(content) + "' WHERE ContentID = " + str(contentID) + ";")
        UpdateData()
        raise cherrypy.HTTPRedirect("/edit")
    @cherrypy.expose
    def EditImg(self, content, contentID, src, remove):
        if(remove == "JA"):
            os.remove(src)
            database.executeCommand("DELETE FROM Images WHERE ImgID = " + str(contentID) +";")
            raise cherrypy.HTTPRedirect("/edit_img")
        if(content.file == None):
            raise cherrypy.HTTPRedirect("/edit_img")
        else:
            os.remove(src)
            with open(src,"wb") as file:
                file.write(content.file.read())
            
            database.executeCommand("UPDATE Images SET src = '" + str(src) + "' WHERE ImgID = " + str(contentID) + ";")
            database.executeCommand("UPDATE Images SET Version = Version + 0.1 WHERE ImgID = " + str(contentID) + ";")
            UpdateData()
            raise cherrypy.HTTPRedirect("/edit_img")
    @cherrypy.expose
    def AddImg(self, content, src):
        if(content.file == None):
            raise cherrypy.HTTPRedirect("/edit_img")
        elif(os.path.isfile("images/" + fix_str(src) + os.path.splitext(content.filename)[1]) or len(src) == 0):
            raise cherrypy.HTTPRedirect("/edit_img?f=1")
        else:
            with open("images/" + fix_str(src) + os.path.splitext(content.filename)[1],"wb") as file:
                file.write(content.file.read())
            
            database.executeCommand("INSERT INTO Images(src, Version) VALUES ('images/" + fix_str(src) + os.path.splitext(content.filename)[1] + "', 1);")
            UpdateData()
            raise cherrypy.HTTPRedirect("/edit_img")
        
USERS = {'Admin':'Password'}

if __name__ == '__main__':
    UpdateData()
    conf = {'/': {'tools.staticdir.on': True,'tools.staticdir.dir':'./','tools.mako.directories':"./", 'tools.staticdir.root': os.path.abspath(os.getcwd()),
                  'tools.encode.on': True,'tools.encode.encoding': 'utf-8','tools.staticfile.filename':"favicon.ico"},
    "global":{'server.socket_host': 'localhost',
                        'server.socket_port': 80,#executeSelect("SELECT port FROM Conf")
                       },
            '/edit': {
        'tools.auth_digest.on': True,
        'tools.auth_digest.realm': 'localhost',
        'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain(USERS),
        'tools.auth_digest.key': 'a565c27146791cfb'
   },
            '/edit_img': {
        'tools.auth_digest.on': True,
        'tools.auth_digest.realm': 'localhost',
        'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain(USERS),
        'tools.auth_digest.key': 'a565c27146791cfb'
   },
            '/EditContent': {
        'tools.auth_digest.on': True,
        'tools.auth_digest.realm': 'localhost',
        'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain(USERS),
        'tools.auth_digest.key': 'a565c27146791cfb'
   },
            '/EditImg': {
        'tools.auth_digest.on': True,
        'tools.auth_digest.realm': 'localhost',
        'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain(USERS),
        'tools.auth_digest.key': 'a565c27146791cfb'
   },
            '/server.py':{
        'tools.auth_digest.on': True,
        'tools.auth_digest.realm': 'localhost',
        'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain({}),
        'tools.auth_digest.key': 'a565c271467123123fb'
   },
            '/main.db':{
        'tools.auth_digest.on': True,
        'tools.auth_digest.realm': 'localhost',
        'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain({}),
        'tools.auth_digest.key': 'a565c271467123123fb'
   },}
    cherrypy.quickstart(Website(), '/', conf)
