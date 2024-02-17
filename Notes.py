import TXTNote
from TXTNote import TXTNote
from Organizer import Organizer
import FileInit


class Notes(Organizer):

    savedDict = {}
    createdBuffer = []
    notes = FileInit.FileWorking.detecting(FileInit.FileWorking.path)

    def showBuffer():
        for i in range(len(Notes.createdBuffer)):
            print(Notes.createdBuffer[i])

    def createNote():
        name=input("\nНазвание: ")
        msg=input("\nТекст заметки: ")
        author=input("\nАвтор заметки: ")
        
        currentNote=TXTNote.__new__(TXTNote)
        TXTNote.__init__(currentNote,name, msg, author)
        Notes.createdBuffer.append(TXTNote.toString(currentNote))
        print(f"Заметка {name} успешно создана!")

    def saveNote(): 
        name=input("\nСохранить заметку как: ")
        currentNote = Notes.createdBuffer.pop()
        dict = Notes.savedDict.update({f"{name}": currentNote})
        FileInit.FileWorking.save(currentNote)
        print(f"\nЗаметка {name} была успешно сохранена!")

    def editNote(): 
        name=input("\nРедактировать заметку (введите название): ")
        temp = Notes.savedDict.get(name)
        print(temp)
        Notes.savedDict.pop(name)
        Notes.savedDict.update({f'{name}': input("\nВведите новый текст заметки: ")})
        print(f"\nЗаметка успешно отредактирована!")

    def deleteNote():
        name=input("Удалить заметку (введите название): ")
        Notes.savedDict.pop(name)
        FileInit.FileWorking.deleting(Notes.notes, name)
        print(f"\nЗаметка {name} успешно удалена!")

    def showNotes():
        FileInit.FileWorking.show(Notes.notes)
        print(f"Список заметок: {Notes.savedDict.items()}")