from flask import request, jsonify
import json

from APP.LOCALISATION_API import bp_localisation
from APP.LOCALISATION_API.services import get_localisation_by_user_and_time


@bp_localisation.route('/get_localisation_on_time', methods=('GET',))
def get_localisation():
    localisation = get_localisation_by_user_and_time()

    return jsonify([i.serialize for i in localisation])
