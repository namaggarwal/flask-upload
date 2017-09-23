import os
from flask import Flask, render_template
from views import pages


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

if os.path.exists("instance/config.py"):
    app.config.from_pyfile('config.py')

if os.environ.get('APP_CONFIG_FILE', None):
    app.config.from_envvar('APP_CONFIG_FILE')


### Flask Configurations ####
app.secret_key = app.config["FLASK_SECRET_KEY"]


### Blueprints Configuration ###
app.register_blueprint(pages)



@app.errorhandler(500)
def error(e):
    return render_template('error.html'), 500
