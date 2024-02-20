import TXTNote
from TXTNote import TXTNote
from Organizer import Organizer
import FileInit


class Notes(Organizer):

    # savedDict = {}
    # createdBuffer = []
    idBank = []
    notes = FileInit.FileWorking.detecting(FileInit.FileWorking.path)

    # def showBuffer():
    #     for i in range(len(Notes.createdBuffer)):
    #         print(Notes.createdBuffer[i])

    def createNote():
        name=input("\nНазвание: ")
        msg=input("\nТекст заметки: ")
        author=input("\nАвтор заметки: ")
        
        currentNote=TXTNote.__new__(TXTNote)
        TXTNote.__init__(currentNote,name, msg, author)
        # Notes.createdBuffer.append(TXTNote.toString(currentNote))
        temp = (TXTNote.toString(currentNote)).split(",")
        print(temp)
        FileInit.FileWorking.adding(Notes.notes, temp[0], temp[1], temp[2], temp[3])
        # FileInit.FileWorking.saving(FileInit.FileWorking.path, Notes.notes)
        print (Notes.notes)
        print(f"Заметка {name} успешно создана!")

    def saveNote(): 
        # name=input("\nСохранить заметку как: ")
        # currentNote = Notes.createdBuffer.pop()
        # dict = Notes.savedDict.update({f"{name}": currentNote})
        # FileInit.FileWorking.save(currentNote)
        # FileInit.FileWorking.save(f"'Название' : " + "'" + {Notes.notes['Название']} + "'" + "'Текст' : " + "'" + {Notes.notes['Текст']} + "'" + "'Автор' : " + "'" + {Notes.notes['Автор']} + "'" + "'" + "'Дата создания' : " + "'" + {Notes.notes['Дата создания']} + "'")
        # FileInit.FileWorking.save(Notes.notes['Название'] + Notes.notes['Текст'] + Notes.notes['Автор'] + Notes.notes['Дата создания'])
        FileInit.FileWorking.saving(FileInit.FileWorking.path, Notes.notes)
        print(f"\nЗаметка {Notes.notes[-1]} была успешно сохранена!")

    def editNote(notes): 
        # name=input("\nРедактировать заметку (введите название): ")
        # temp = Notes.savedDict.get(name)
        # print(temp)
        # Notes.savedDict.pop(name)
        # Notes.savedDict.update({f'{name}': input("\nВведите новый текст заметки: ")})
        FileInit.FileWorking.editing(notes)
        FileInit.FileWorking.saving(FileInit.FileWorking.path, notes)
        print(f"\nРедактирование завершено!")

    def deleteNote():
        name=input("Удалить заметку (введите название): ")
        # Notes.savedDict.pop(name)
        FileInit.FileWorking.deleting(Notes.notes, name)
        FileInit.FileWorking.saving(FileInit.FileWorking.path, Notes.notes)
        print(f"\nЗаметка {name} успешно удалена!")

    def showNotes():
        flag = True
        print("Режимы: 1 - показать все заметки,  ")
        print("        2 - найти заметку по дате: ")
        choice = int(input("Введите номер режима(1/2): "))

        while (flag):
            if (choice == 1):
                print(f"Список заметок: ")
                FileInit.FileWorking.show(Notes.notes)
                flag = False
            if (choice == 2):
                date = input("Введите дату заметки (в формате yyyy-mm-dd): ")
                notes = Notes.notes
                for line in notes:
                    value = line['Дата создания'].split(" ")[0]
                    print(value)
                    if (value == date):
                        print(f"Заметкa по дате {date}: {line}")
                flag = False
            else : 
                print("Такого режима нет! проверьте правильность введённой информации (доступно 1 или 2)")
                flag = False
            

    

    # def toString(notes):
    #     for line in notes:
    #         data = line.strip().split(',')
    #         return str(data[0]) + str(data[1]) + str(data[2]) + str(data[3])
