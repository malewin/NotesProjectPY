import TXTNote.py

class Notes(Organizer):

    savedDict = {}
    createdBuffer = []


    def createNote(self, name=input("\nНазвание: "), msg=input("\nТекст заметки: "), author=input("\nАвтор заметки")):
        super.createdBuffer.append(TXTNote.__init__(name, msg, author))
        print(f"Заметка {name} успешно создана!")

    def saveNote(self, name=input("\nСохранить заметку как: ")): 
        super.savedDict.update({f'{name}': super.createdBuffer.pop()})
        print(f"\nЗаметка {name} была успешно сохранена!")

    def editNote(self, name=input("\nРедактировать заметку (введите название): ")): 
        temp = super.savedDict.get(name)
        print(temp)
        super.savedDict.pop(name)
        super.savedDict.update({f'{name}': input("\nВведите новый текст заметки: ")})
        print(f"\nЗаметка успешно отредактирована!")

    def deleteNote(self, name=input("Удалить заметку (введите название): ")):
        super.savedDict.pop(name)
        print(f"\nЗаметка {name} успешно удалена!")

    def showNotes(self):
        print(f"Список заметок: {super.savedDict.items()}")