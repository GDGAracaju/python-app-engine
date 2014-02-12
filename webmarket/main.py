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


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
