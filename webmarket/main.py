# coding: utf-8
import os

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
        produtos_query = Produto.query(ancestor=ndb.Key('Produto', 'webmarket'))
        produtos = produtos_query.fetch(10)
        
        valores_template = {'produtos': produtos}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(valores_template))


class AdicionarProdutoHandler(webapp2.RequestHandler):
    def post(self):
        produto = Produto(parent=ndb.Key('Produto', 'webmarket'))
        produto.descricao = self.request.get('descricao')        
        produto.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AdicionarProdutoHandler)
], debug=True)
