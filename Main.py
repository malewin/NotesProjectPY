import Notes
from Notes import Notes
import FileInit

status = True


while (status):
    print("____________________________")
    print("||||||||| ЗАМЕТКИ |||||||||")
    print("Меню: 1 - Создать заметку")
    print("      2 - Сохранить заметку")
    print("      3 - Редактировать заметку")
    print("      4 - Удалить заметку")
    print("      5 - Показать список заметок")
    print("      6 - Выйти из приложения")
    print("____________________________")

    currentInput = input("Введите номер пункта меню: ")
    if (currentInput == "1"):
        print("---> 1")
        Notes.createNote()
    elif (currentInput == "2"):
        print("---> 2")
        Notes.saveNote()
    elif (currentInput == "3"):
        print("---> 3")
        Notes.editNote()
    elif (currentInput == "4"):
        print("---> 4")
        Notes.deleteNote()
    elif (currentInput == "5"):
        print("---> 5")
        Notes.showNotes()
    elif (currentInput == "6"):
        status = False
        break
    

