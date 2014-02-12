from google.appengine.api import users
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.write('Hello %s!' % user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
