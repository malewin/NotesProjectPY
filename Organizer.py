import abc

class Organizer(abc.ABC):
    
    @abc.abstractmethod
    def createNote(self): pass

    @abc.abstractmethod
    def saveNote(self): pass

    @abc.abstractmethod
    def editNote(self): pass

    @abc.abstractmethod
    def deleteNote(self): pass

    

