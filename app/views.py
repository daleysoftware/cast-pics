import flask

from . import app, image_selector


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/next')
def next():
    return image_selector.next()
