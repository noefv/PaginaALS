
from google.appengine.ext import ndb



class Coments(ndb.Model):

    comentary = ndb.TextProperty(indexed=True)
    game_id = ndb.TextProperty(indexed=True)
    user_email = ndb.TextProperty(indexed=True)
    puntuacion = ndb.IntegerProperty(indexed=True)


def create_empty_comentary():
    """Used when there the user is not important."""
    return Coments(comentary="", game_id="", user_email="")


@ndb.transactional
def update(comentary):
    """Updates a user.

        :param user: The user to update.
        :return: The key of the record.
    """
    return comentary.put()

