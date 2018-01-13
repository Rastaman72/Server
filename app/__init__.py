import os
import shutil
from flask import Flask, request, render_template, redirect, flash
from app.extras.scripts.label_image import runImageFile
from werkzeug import secure_filename
import csv

from os import listdir
from os.path import isfile, join
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = "/My/Studia/Magisterka/PROEJCT/app/"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/analyzeNormalImage', methods=['GET'])
def analyzeNormalImage():
    mypath = "/My/Studia/Magisterka/PROEJCT/app/extras/faces"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file = open(mypath+'result.txt', 'a+')

    for filename in onlyfiles:
        if allowed_file(filename):
            result = runImageFile(filename)
            print(result)
            file.write(result+ '\n')
    return "onlyfiles"


@app.route('/uploadFiles', methods=['GET', 'POST'])
def uploadNewfile():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = runImageFile(filename)
            print
            # print(result)
            # print(result[1])
            # src = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # dst = os.path.join(app.config['UPLOAD_FOLDER'], "/extras/test",result[1],"/",filename)
            # shutil.copy(src, dst)
            return 'file uploaded successfully' + "\n" + result[0]
            # return redirect(url_for('uploaded_file', filename=filename))
    return "File not found"


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_fileR():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result = runImageFile(filename)
        print(result)
        return 'file uploaded successfully' + "\n" + result


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True)
