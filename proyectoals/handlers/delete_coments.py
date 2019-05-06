import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

from model.coments import Coments


class ComentsDelete(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        access_link = users.create_logout_url("/")

        id = int(self.request.get("id"))
        coment = Coments.get_by_id(id)

        template_values = {
            "user": user.nickname(),
            "access_link": access_link
        }

        if coment and user.email() == coment.user_email or user.email() == "noe_ferreiro@hotmail.com":
            coment.key.delete()

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("confirm.html", **template_values))

        else:

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("error.html", **template_values))


app = webapp2.WSGIApplication([
    ('/delete_coments', ComentsDelete),
], debug=True)
