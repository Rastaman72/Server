import os
from flask import Flask, request, redirect, url_for
from app.extras.scripts.label_image import runImageFile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


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
