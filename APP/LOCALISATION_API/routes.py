from flask import request, jsonify
import json

from APP.LOCALISATION_API import bp_localisation
from APP.LOCALISATION_API.services import get_localisation_by_user_and_time, get_last_localisation_by_user


@bp_localisation.route('/get_localisation_on_time', methods=('GET',))
def get_localisation():
    localisation = get_localisation_by_user_and_time()

    return jsonify([i.serialize for i in localisation])


@bp_localisation.route('/get_last_localisation', methods=('GET',))
def get_last_localisation():
    localisation = get_last_localisation_by_user()

    return jsonify(localisation.serialize)
