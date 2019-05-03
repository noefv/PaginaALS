
from google.appengine.ext import ndb



class Games(ndb.Model):

    name = ndb.TextProperty(indexed=True)
    code = ndb.TextProperty(indexed=True)
    type = ndb.TextProperty(indexed=True)
    platform = ndb.TextProperty(indexed=True)


def create_empty_game():
    """Used when there the user is not important."""
    return Games(name="", code="", type="", platform="")


@ndb.transactional
def update(game):
    """Updates a user.

        :param user: The user to update.
        :return: The key of the record.
    """
    return game.put()

