import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

from model.coments import Coments
from model.games import Games
import model.games as game_mgt


class GamesDelete(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")

            id = int(self.request.get("id"))
            game = Games.get_by_id(id)

            template_values = {
                "user": user.nickname(),
                "access_link": access_link,
                "game": game
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("delete_games.html", **template_values))
        else:
            self.redirect("/")
            return

    def post(self):
        user = users.get_current_user()
        access_link = users.create_logout_url("/")

        id = int(self.request.get("id"))
        game = Games.get_by_id(id)

        template_values = {
            "user": user.nickname(),
            "access_link": access_link,
            "msg": "You can't delete a game added by other user."
        }

        if game and user.email() == game.user_email or user.email() == "noe_ferreiro@hotmail.com":
            coment = Coments.query(Coments.game_id == str(id))
            coment = list(coment)

            for comen in coment:
                comen.key.delete()

            game.key.delete()

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("confirm.html", **template_values))

        else:

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("error.html", **template_values))

app = webapp2.WSGIApplication([
    ('/delete_games', GamesDelete),
], debug=True)
