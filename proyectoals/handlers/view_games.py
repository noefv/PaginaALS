import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2
from model.games import Games
import model.games as game_mgt
from model.coments import Coments
import model.coments as coment_mgt


class GamesView(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")

            id = int(self.request.get("id"))
            game = Games.get_by_id(id)

            coment = Coments.query(Coments.game_id == str(id))
            coment = list(coment)

            template_values = {
                "user": user.nickname(),
                "access_link": access_link,
                "game": game,
                "coment": coment,
                "admin": "noe_ferreiro@hotmail.com"
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("view_games.html", **template_values))
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/view_games', GamesView),
], debug=True)
