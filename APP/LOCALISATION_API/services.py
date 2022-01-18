from APP import db
from APP.LOCALISATION_API.models import Localisation


def get_localisation_by_user_and_time():
    r = Localisation.query.all()

    return r


def get_last_localisation_by_user():
    r = Localisation.query.order_by(Localisation.id.desc()).first()

    return r
