import cherrypy
from cherrypy.lib import auth_digest
import os, os.path
from mako.template import Template

class Website(object):
    @cherrypy.expose
    def index(self):
        return Template(open('index.html').read().encode("cp1252","ignore")).render()
        
        
if __name__ == '__main__':
    conf = {'/': {'tools.staticdir.on': True,'tools.staticdir.dir':'./','tools.mako.directories':"./", 'tools.staticdir.root': os.path.abspath(os.getcwd()),
                  'tools.encode.on': True,'tools.encode.encoding': 'utf-8','tools.staticfile.filename':"favicon.ico"},}
    cherrypy.config.update({'server.socket_host': 'localhost',
                        'server.socket_port': 80,
                       })
    cherrypy.quickstart(Website(),'/', conf)

