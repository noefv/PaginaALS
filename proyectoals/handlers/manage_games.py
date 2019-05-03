import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2
from model.games import Games


class GamesManager(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")

            all_games = Games.query()
            all_games = list(all_games)

            template_values = {
                "user": user.email(),
                "access_link": access_link,
                "games": all_games
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("games.html", **template_values))
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/manage_games', GamesManager),
], debug=True)
