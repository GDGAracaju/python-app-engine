# coding: utf-8

import webapp2

MAIN_PAGE_HTML = """\
<html>
  <body>
    <h1>App Engine WebMarket</h1>
    <h2>Adicionar produto</h2>
    <form action="/add" method="post">
      <div><label for="descricao">Descrição</label> <input type="text" name="descricao"></div>
      <div><input type="submit" value="Adicionar"></div>
    </form>
  </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class AdicionarProdutoHandler(webapp2.RequestHandler):
    def post(self):
        produto = self.request.get('descricao')        
        self.response.write('Você adicionou: ')
        self.response.write('<strong>%s</strong>' % produto)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AdicionarProdutoHandler)
], debug=True)
