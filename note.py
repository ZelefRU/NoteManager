from datetime import datetime


class Note(object):

    def __init__(self, body, title):
        self.date = datetime.now()
        self.id = id(self.date)
        self.body = body
        self.title = title