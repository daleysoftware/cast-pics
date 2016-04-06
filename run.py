from app import app, s
import threading


class Flask(object):
    def __init__(self, app):
        self.app = app
    def _func_to_be_threaded(self):
        self.app.run(port=8989)
    def start(self):
        threading.Thread(target=self._func_to_be_threaded).start()


class Scheduler(object):
    def __init__(self, s):
        self.s = s
    def _func_to_be_threaded(self):
        self.s.run()
    def start(self):
        threading.Thread(target=self._func_to_be_threaded).start()


class ChromecastBroadcaster(object):
    def __init__(self):
        pass
    def _func_to_be_threaded(self):
        self.s.run()
    def start(self):
        threading.Thread(target=self._func_to_be_threaded).start()


if __name__ == '__main__':
    Flask(app).start()
    Scheduler(s).start()
