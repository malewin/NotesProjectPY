import datetime

from TheNote import TheNote

class TXTNote(TheNote):

    def toString(self):
        return "Название: " + str(self.name) + "; Текст: " + str(self.msg) + "; Автор: " + str(self.author) + "; Время создания: " + str(self.timeOfCreate)
    

    def __new__(self, *args, **kwargs):
        print("Создан экземпляр класса TXTNote")
        return super().__new__(self)
    
    def __init__(self, name, msg, author):
        self.name = name
        self.msg = msg
        self.author = author
        self.timeOfCreate = datetime.datetime.now()


    