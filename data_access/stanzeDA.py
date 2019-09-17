from google.appengine.ext import ndb

from models.stanzeModel import Stanza


def getAllStanze():
    stanze = Stanza().query().fetch()
    return stanze


def getStanza(stanza_id):
    stanza = Stanza().query(Stanza.stanza_id==stanza_id).fetch(1)
    return stanza