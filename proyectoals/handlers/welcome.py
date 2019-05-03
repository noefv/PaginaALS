# (c) Noe Ferreiro Vazquez 2019 <nfvazquez17@esei.uvigo.es>

import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2


class WelcomePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.redirect("/manage_games")
            return
        else:
            access_link = users.create_login_url("/manage_games")
            template_values = {
                "user": "Iniciar Sesion",
                "access_link": access_link
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
    ('/', WelcomePage),
], debug=True)
