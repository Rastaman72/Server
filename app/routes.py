from app import app
from flask import request

from app.extras.scripts.label_image import runImageFile
from werkzeug import secure_filename


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/script/<imageName>')
def script(imageName):
    result = runImageFile(imageName)
    print(result)
    return result
