# -*- coding: utf-8 -*-

import os

from flask                      import Flask
from flask_sslify               import SSLify
from flask.ext                  import restful
from werkzeug.contrib.fixers    import ProxyFix
from config                     import env_config
from mongoengine                import connect
from server.models.user         import User
from server.resources.users     import UserList, User

# For import *
__all__ = ['create_app']


def create_app():
    """Create a Flask app."""

    app_name = "scaffolding"
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web/static")

    app = Flask(app_name, static_folder=static_dir)

    configure_app(app)

    configure_extensions(app)

    configure_apis(app)

    configure_mongodb(app)

    return app

def configure_app(app):
    app.config.from_object('config.default')
    app.config.from_object(env_config)


def configure_extensions(app):
    app.current_env = os.environ.get('APPLICATION_ENV', 'development')
    app.secret_key = app.config.get('SESSION_SECRET')

    # Force SSL if not in dev.
    if app.current_env in ('production', 'staging'):
        SSLify(app, permanent=False)

    app.wsgi_app = ProxyFix(app.wsgi_app)


def configure_apis(app):
    api = restful.Api(app)
    api.add_resource(UserList, '/')
    api.add_resource(User, '/users/<string:user_id>')

def configure_mongodb(app):
    db_name = app.config.get('APPLICATION_MONGODB_DBNAME', "scaffolding-{}".format(os.environ.get('APPLICATION_ENV', 'development')))
    db_uri = app.config.get('APPLICATION_MONGODB_URI', "mongodb://{}:{}/{}".format(
        app.config.get('APPLICATION_MONGODB_HOST'),
        app.config.get('APPLICATION_MONGODB_PORT'),
        app.config.get('APPLICATION_MONGODB_DBNAME')
    ))
    connect(db_name, host=db_uri)


app = create_app()


if __name__ == '__main__':
    app.run(host=app.config.get('HOST', '0.0.0.0'), port=app.config.get('PORT', 5000), debug=app.config.get('DEBUG', False))
