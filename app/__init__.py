import flask

from . import images

app = flask.Flask(__name__)

image_selector = images.ImageSelector()
image_selector.refresh()

from . import views


import sched
import time

s = sched.scheduler(time.time, time.sleep)

# Every hour.
REFRESH_SECONDS = 60 * 60
s.enter(REFRESH_SECONDS, 1, image_selector.refresh)
