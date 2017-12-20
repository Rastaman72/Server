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


@app.route('/uploadImage')
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
