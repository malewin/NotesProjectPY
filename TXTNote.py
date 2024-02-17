import abc
import datetime

from notificationExamPY.TheNote import TheNote

class TXTNote(TheNote):

    def __init__(self, name, msg, author):
        self.name = name
        self.msg = msg
        self.author = author
        self.timeOfCreate = datetime.now()

    