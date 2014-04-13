import logging
import traceback

from flask import session, current_app, abort, jsonify, request
from functools import wraps


def basic_authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' not in session or 'password' not in session:
            auth = request.authorization
            password = current_app.config.get('PASSWORD')

            if auth and auth.username \
                    and auth.password != '' \
                    and auth.password == password:
                print("User '{}' has logged in via basic auth".format(auth.username))
                session['username'] = auth.username
                session['password'] = auth.password
        if not session.get('username') or not session.get('password'):
            return abort(403)
        return f(*args, **kwargs)
    return decorated


def json_response(f):
    @wraps(f)
    def send_response(*args, **kwargs):
        status_code = 200
        try:
            data = f(*args, **kwargs)
            if data is None:
                data = {
                    "err": "No data is available.",
                    "hasError": True
                }
                status_code = 404
        except Exception as e:
            error_message = "Unexpected error: '{}'".format(e)
            logging.error(error_message)
            traceback.print_exc()

            data = {"err": error_message, "hasError": True}
            status_code = 500

        return jsonify(data), status_code

    return send_response