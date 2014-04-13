#!/usr/bin/env python

from flask.ext.script   import Server, Manager
from app                import app

# Flask-Script is the Flask command line script runner:
# http://flask-script.readthedocs.org/en/latest/
manager = Manager(app)

server = Server(host="0.0.0.0", port=app.config.get('PORT'))

manager.add_command("runserver", server)

if __name__ == "__main__":
    manager.run()