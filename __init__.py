from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from .modules import Classifier
from .modules.Logger import *
from random import randint
import os

app = Flask(__name__)
# app.secret_key = environ.get() #
# app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 # Max image upload is 50MB
app.config.update(
    SECRET_KEY = os.environ.get('SECRET_KEY'),
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
)

@app.route('/')
def index():
    return render_template('index.html')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return True

    log('[delete_file] File not found: %s' % file_path)
    return False

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        flash('An error occurred!')
        return redirect('/')

    file = request.files['file']
    if file.filename == '':
        flash('No selected file!')
        return redirect('/')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.root_path, "tmp", filename)
        file.save(path)
        error = False
        try:
            result = Classifier.classify(path)
        except:
            log('[classify] Error in classification')
            error = True
        finally:
            delete_file(path)

        if not error:
            return redirect(url_for('details', tree=result))

    flash('An error occurred!')
    return redirect('/')

@app.route('/tree/<tree>')
def details(tree):
    data = {
        'tree': tree,
        'name': Classifier.TYPES[int(tree)].capitalize(),
        'descript': Classifier.DESCRIPTION[int(tree)]
    }
    return render_template('details.html', data=data)

# Displays random tree to user
@app.route('/random')
def random():
    tree = randint(0, 13)
    return redirect(url_for('details', tree=tree))

# Adds website favicon image
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run()
