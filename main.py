from flask import Flask, render_template, send_file, abort, session
import random
import os
import time
import re

here = os.path.dirname(__file__)
def path(rel): return os.path.join(here, rel)

print(os.listdir(path('static/img/home/')))

app = Flask(__name__, template_folder=path('pages/'))
content_urls = {
    'bald.jpg': '/content/liftoff',
    'IMG_20191019_004248.jpg': '/content/chavs',
    'movie.jpg': '/content/letmego',
    '20200102_223247.jpg': '/content/rage',
    'Asset0019.jpg': '/content/romil',
    '20190614_235009.jpg': '/content/space',
    'IMG_1695.jpg': '/content/tyla',
    'drnk.jpg': '/content/fountain'
}

@app.before_request
def before_request():
    if 'title' not in session or session['expires'] < time.time():
        title = 'static/img/title/' + random.choice(os.listdir(path('static/img/title/')))
        session['title'] = title
        session['expires'] = time.time() + 600 # ten minutes

@app.route('/')
def welcome():
    home = 'static/img/home/' + random.choice(os.listdir(path('static/img/home/')))
    return render_template('entrance.html', title=session['title'], home=home)

@app.route('/fatnipple1.html')
def fatnipple1():
    files = os.listdir(path('static/img/home/'))
    all_images = [ {
        'src': '/static/img/home/' + fn,
        'url': content_urls[fn] if fn in content_urls else '#'
    } for fn in files ]
    return render_template('fatnipple1.html', title=session['title'], images=all_images)

@app.route('/content/<page>')
def content(page):
    safe_page = re.sub(r'\W+', '', page)
    return render_template('content/%s.html' % safe_page)

if __name__ == '__main__':
    app.secret_key = 'totally secret secret key'
    app.run(host='0.0.0.0', port=8000, debug=True)