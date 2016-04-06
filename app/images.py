import fnmatch
import random
import os
import urllib.parse


# Assume the images we want to cycle through are located in the 'static' directory.
STATIC_ASSETS_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

IMAGES_COUNT = 100

class ImageSelector(object):

    def __init__(self):
        self.images = None
        self.refresh()


    @staticmethod
    def _format_filename(root, filename):
        return urllib.parse.quote(
            os.path.join(root, filename).replace(STATIC_ASSETS_DIRECTORY, '/static'))


    def refresh(self):
        matches = []
        for root, dirnames, filenames in os.walk(STATIC_ASSETS_DIRECTORY):
            for filename in fnmatch.filter(filenames, '*.[jJ][pP][gG]'):
                matches.append(
                    (ImageSelector._format_filename(root, filename),
                     os.path.getctime(os.path.join(root, filename))))
        # Sorted by recency, and choose the last segment of images.
        self.images = [x[0] for x in sorted(matches, key=lambda x: x[1], reverse=True)[0:IMAGES_COUNT]]


    def next(self):
        return random.choice(self.images)