from flask import Flask, render_template, send_file, abort
from lib import security
import random
import os

app = Flask(__name__, template_folder='pages/')

images = []
for root, dirs, files in os.walk('img/'):
    norm = lambda f: os.path.normpath(root + '/' + f).replace('\\', '/')
    images.extend(norm(f) for f in files)

@app.route('/img/<path:img>')
def image(img):
    filepath = 'img/' + img
    if filepath in images: return send_file(filepath)
    else: abort(404)

@app.route('/')
def index():
    title = '/img/title/title (%s).jpg' % random.randint(1, 4)
    home = '/img/home/home (%s).jpg' % random.randint(1, 31)
    return render_template('index.html', title=title, home=home)

app.run(host='0.0.0.0', port=8000)