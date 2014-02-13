# coding: utf-8
import os

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Produto(ndb.Model):
    descricao = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        produtos_query = Produto.query(ancestor=ndb.Key('Catalogo', 'webmarket'))
        produtos = produtos_query.fetch(10)

        user = users.get_current_user()
        nome = None
        if user:
            nome = user.nickname()
            url = users.create_logout_url(self.request.uri)
            texto_link = 'Sair'
        else:
            url = users.create_login_url(self.request.uri)
            texto_link = 'Entrar'
        
        valores_template = {'produtos': produtos,
                            'nome': nome,
                            'url': url,
                            'texto_link': texto_link}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(valores_template))


class AdicionarProdutoHandler(webapp2.RequestHandler):
    def post(self):
        produto = Produto(parent=ndb.Key('Catalogo', 'webmarket'))
        produto.descricao = self.request.get('descricao')        
        produto.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AdicionarProdutoHandler)
], debug=True)
