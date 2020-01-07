from flask import Flask, render_template
import random
app = Flask(__name__, template_folder='pages/')

@app.route('/')
def index():
    title = '/static/img/title/title (%s).jpg' % random.randint(1, 4)
    home = '/static/img/home/home (%s).jpg' % random.randint(1, 31)
    return render_template('index.html', title=title, home=home)

app.run(host='0.0.0.0', port=8000)