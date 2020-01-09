from flask import Flask, render_template, send_file, abort, session
from lib import security
import random
import os
import time

app = Flask(__name__, template_folder='pages/')
app.secret_key = security.app_secret_key()

images = []
for root, dirs, files in os.walk('img/'):
    norm = lambda f: os.path.normpath(root + '/' + f).replace('\\', '/')
    images.extend(norm(f) for f in files)

@app.before_request
def before_request():
    if 'title' not in session or session['expires'] < time.time():
        title = 'img/title/' + random.choice(os.listdir('img/title/'))
        session['title'] = title
        session['expires'] = time.time() + 600 # ten minutes

@app.route('/img/<path:img>')
def image(img):
    filepath = 'img/' + img
    if filepath in images: return send_file(filepath)
    else: abort(404)

@app.route('/')
def welcome():
    home = 'img/home/' + random.choice(os.listdir('img/home/'))
    return render_template('entrance.html', title=session['title'], home=home)

@app.route('/fatnipple1.html')
def fatnipple1():
    all_images = [ 'img/home/' + fn for fn in os.listdir('img/home/') ]
    return render_template('fatnipple1.html', title=session['title'], images=all_images)

app.run(host='0.0.0.0', port=8000, debug=True)