import datetime
import os
import Notes
import csv
import pandas as pd


class FileWorking:

    path = '/Users/viktortarkhanov/Desktop/notificationExamPY/Notes.csv'

    def save(self):
        with open(FileWorking.path, 'w+') as data:
                data.write(self)

    def saving(fileSourse, notes):
        with open(fileSourse, 'w+') as file:
            for note in notes:
                df = pd.DataFrame({f"'id' : ['{note['id']}'], 'Название' : ['{note['Название']}'], 'Текст' : ['{note['Текст']}'], 'Автор' : ['{note['Автор']}'], 'Дата создания' : ['{note['Дата создания']}']"})
                # temp = str(note.keys())
                # if temp == "dict_keys(['id', 'Название', 'Текст', 'Автор', 'Дата создания'])":
                #     pass
                df.to_csv(file)
    
    def detecting(fileSourse):
        notes = []
        if os.path.exists(fileSourse):
            with open(fileSourse, 'r') as file:
                csvReader = csv.reader(file)
                for line in csvReader:
                    data = line.strip().split(',')
                    # try: data = line.strip().split(',')
                    # finally: print(data)
                    notes.append({'Название': data[0], 'Текст': data[1], 'Автор': data[2], 'Дата создания': data[3]})
        return notes
    
    def adding(notes, name, msg, author, date):
        notes.append({'id' : Notes.Notes.idBank[-1], 'Название': name, 'Текст': msg, 'Автор': author, 'Дата создания': date})

    def deleting(notes, id):
        notes[:] = [note for note in notes if note['id'] != id]

    def show(notes):
        if len(notes) > 0:
            for note in notes:
                print(f"id: {note['id']}, Название: {note['Название']}, Текст: {note['Текст']}, Автор: {note['Автор']}, Дата рождения: {note['Дата создания']}")
        else: print(f"Файл не найден или еще не создан")

    def editing(notes):
        name = input("Введите название заметки, которую хотите отредактировать: ")
        editedMsg = input("Текст: ")
        newAuthor = input("Автор: ")
        for note in notes:
            if note['Название'].lower() == name.lower():
                note['Текст'] = editedMsg
                note['Автор'] = newAuthor
                note['Дата создания'] = datetime.datetime.now()
                print(note)
            else: 
                print("Такой заметки нет")
                break


    
