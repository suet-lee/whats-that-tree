import torch
from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import modules.Classifier
# from werkzeug.datastructures import FileStorage

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def index():
    a = Classifier.get_class(2)
    print(a)
    flash('Test')
    return render_template('test.html')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        flash('Error occurred!')
        return redirect('/')

    file = request.files['file']
    if file.filename == '':
        flash('No selected file!')
        return redirect('/')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename)
        return Classifier.classify(file)

        return filename
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))
    return ''
