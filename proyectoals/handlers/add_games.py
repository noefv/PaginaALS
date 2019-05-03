import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2
from model.games import Games
import model.games as game_mgt


class GamesAdd(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")

            template_values = {
                "user": user.email(),
                "access_link": access_link
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("add_games.html", **template_values))
        else:
            self.redirect("/")
            return

    def post(self):
        user = users.get_current_user()
        access_link = users.create_logout_url("/")

        template_values = {
            "user": user.email(),
            "access_link": access_link
        }

        game = game_mgt.create_empty_game()
        game.code = self.request.get("code")
        game.name = self.request.get("name")
        game.type = self.request.get("type")
        game.platform = self.request.get("platform")

        if game:
            game_mgt.update(game)

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("confirm.html", **template_values))
        else:
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("error.html", **template_values))

app = webapp2.WSGIApplication([
    ('/add_games', GamesAdd),
], debug=True)
