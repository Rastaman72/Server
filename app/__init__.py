import os
from flask import Flask, request, render_template
from app.extras.scripts.label_image import runImageFile
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/My/Studia/Magisterka/PROEJCT/app"


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/script/<imageName>')
def script(imageName):
    result = runImageFile(imageName)
    print(result)
    return result


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
    app.run(debug=True)
