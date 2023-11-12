from note import Note

from datetime import datetime


class Notebook(object):
    def __init__(self):
        self.new_list = []

    def recording_to_file(self):
        with open('file.json', 'w', encoding='utf-8') as f:
            for note in self.new_list:
                f.write(f"{note.date}\n ID: {note.id}\n Title: {note.title}\n Body: {note.body}\n\n")

    def save_note(self):
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                count = len(f.readlines())
                with open('file.json', 'r', encoding='utf-8') as f2:
                    i = 0
                    while i < count:
                        line = f2.readline()
                        if line == '\n':
                            i += 1
                        else:
                            save_note = Note("", "")
                            save_note.date = datetime.strptime(line.rstrip('\n'), '%Y-%m-%d %H:%M:%S.%f')
                            i += 1
                            save_note.id = int(f2.readline().lstrip('ID: ').rstrip('\n'))
                            i += 1
                            save_note.title = f2.readline().lstrip('Title: ').rstrip('\n')
                            i += 1
                            save_note.body = f2.readline().lstrip('Body: ').rstrip('\n')
                            i += 1
                            self.new_list.append(save_note)
                    self.recording_to_file()
        except:
            new_file = open('file.json', 'w', encoding='utf-8')
            new_file.close()
            print("\nChoose note: ")
        else:
            print("\nFile note found\n")
