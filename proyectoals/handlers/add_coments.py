import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2
from model.games import Games
import model.games as game_mgt
from model.coments import Coments
import model.coments as coment_mgt


class ComentsAdd(webapp2.RequestHandler):

    def post(self):
        user = users.get_current_user()
        access_link = users.create_logout_url("/")

        id = int(self.request.get("id"))
        game = Games.get_by_id(id)

        try:
            estrellas = int(self.request.get("estrellas"))
        except:
            estrellas = 0

        coment = coment_mgt.create_empty_comentary()
        coment.comentary = self.request.get("txtarea")
        coment.user_email = user.email()
        coment.puntuacion = estrellas
        coment.game_id = str(id)

        template_values = {
            "user": user.nickname(),
            "access_link": access_link,
            "game": game,
            "coment": coment
        }

        if game:
            coment_mgt.update(coment)

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("confirm.html", **template_values))
        else:
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("error.html", **template_values))

app = webapp2.WSGIApplication([
    ('/add_coments', ComentsAdd),
], debug=True)
