import abc

class TheNote(abc.ABC):
    
    @abc.abstractmethod
    def __init__(self, name, msg, author): 
        pass

    @abc.abstractmethod
    def toString():
        pass

    