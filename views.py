from flask import Blueprint, render_template, request, current_app as app
from werkzeug.utils import secure_filename
import os
from build import Build

pages = Blueprint('pages', __name__,template_folder='templates')

ALLOWED_EXTENSIONS = set(['zip'])

@pages.route("/")
def home():
    return render_template("home.html")


@pages.route("/upload", methods=['POST'])
def upload():
    file = request.files['build']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        bObj = Build()
        bObj.build(app.config["UPLOAD_FOLDER"],app.config['UNZIP_FOLDER'],app.config["FILE_NAME"])
    return render_template("success.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


