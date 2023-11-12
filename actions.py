from note import Note
from note_saver import Notebook
from datetime import datetime


class Operations(object):
    def __init__(self):
        self.new_book = Notebook()
        self.new_book.save_note()

    def add_note(self):
        title = input("\n Choose note title: \n")
        body = input("\n Choose note description: \n")
        new_note = Note(body, title)
        self.new_book.new_list.append(new_note)
        self.new_book.recording_to_file()

    def read_notes(self):
        if (len(self.new_book.new_list) == 0):
            print("\n Note list empty \n")
        else:
            for note in self.new_book.new_list:
                print(f"\n{note.date}\n ID: {note.id}\n Title: {note.title}\n Body: {note.body}\n\n")

    def print_by_id(self, input_id):
        for note in self.new_book.new_list:
            if note.id == input_id:
                print(f"\n{note.date}\nID: {note.id}\nTitle: {note.title}\nBody: {note.body}\n\n")
                return True
            else:
                continue
        print("Note not found!")
        return False

    def get_by_date(self, date):
        flag = False
        for note in self.new_book.new_list:
            if note.date.strftime("%d-%m-%Y") == date:
                print(f"\n {note.date}\n ID: {note.id}\n Title: {note.title}\n Body: {note.body}\n\n")
                flag = True
                continue
            else:
                continue
        if (flag == False): print("\n Note with this date not found")

    def delete_note(self, id):
        for note in self.new_book.new_list:
            if note.id == id:
                self.new_book.new_list.remove(note)
                print("File saved")
            self.new_book.recording_to_file()

    def change_title(self, id, new_text):
        for note in self.new_book.new_list:
            if note.id == id:
                note.title = new_text
                print("\n Title hs been changed \n")
            note.new_book.recordingToFile()

    def change_body(self, id, new_text):
        for note in self.new_book.new_list:
            if note.id == id:
                note.body = new_text
                print("\n Note descriptions has been changed \n")
            note.new_book.recordingToFile()
