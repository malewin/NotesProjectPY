import datetime

from TheNote import TheNote

class TXTNote(TheNote):

    def toString(self):
        return str(self.name) + "," + str(self.msg) + "," + str(self.author) + "," + str(self.timeOfCreate)
    

    def __new__(self, *args, **kwargs):
        print("Создан экземпляр класса TXTNote")
        return super().__new__(self)
    
    def __init__(self, name, msg, author):
        self.name = name
        self.msg = msg
        self.author = author
        self.timeOfCreate = datetime.datetime.now()
        


    