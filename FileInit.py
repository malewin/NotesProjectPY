import datetime
import os


class FileWorking:

    path = '/Users/viktortarkhanov/Desktop/notificationExamPY/Notes.txt'

    def save(self):
        with open(FileWorking.path, 'w+') as data:
                data.write(self)

    def saving(fileSourse, notes):
        with open(fileSourse, 'w+') as file:
            for note in notes:
                file.write(f"'Название' : {note['Название']}, 'Текст' : {note['Текст']}, 'Автор' : {note['Автор']}, 'Дата создания' : {note['Дата создания']}\n")
    
    def detecting(fileSourse):
        notes = []
        if os.path.exists(fileSourse):
            with open(fileSourse, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    # try: data = line.strip().split(',')
                    # finally: print(data)
                    notes.append({'Название': data[0], 'Текст': data[1], 'Автор': data[2], 'Дата создания': data[3]})
        return notes
    
    def adding(notes, name, msg, author, date):
        notes.append({'Название': name, 'Текст': msg, 'Автор': author, 'Дата создания': date})

    def deleting(notes, name):
        notes[:] = [note for note in notes if note['Название'].lower() != name.lower()]

    def show(notes):
        if len(notes) > 0:
            for note in notes:
                print(f"{note['Название']},{note['Текст']},{note['Автор']},{note['Дата создания']}")
        else: print(f"Файл не найден или еще не создан")

    def editing(notes, name, msg, author):
        for note in notes:
            if note['Название'].lower() == name.lower():
                note['Текст'] = msg
                note['Автор'] = author
                note['Дата создания'] = datetime.datetime.now()

    
