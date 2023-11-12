from actions import Operations


class Start(object):
    menu = ('Actions: \n'
            + '1 - Add note \n'
            + '2 - Show all notes \n'
            + '3 - Search notes by date \n'
            + '4 - Delete notes \n'
            + '5 - Replace data \n'
            + '0 - Exit \n')

    menu_change = ("\n1 -> edit note title \n"
                   + "2 -> edit note description \n"
                   + "3 -> back to menu \n\n"
                   + "Input: ")

    new_text = ("\n Input new text -> ")
    input_id = ("\n Input note ID -> ")
    input_date = ("\n Input date (format dd-mm-yyyy) for sort notes -> ")

    def __init__(self):
        self.main = Operations()

    def choose(self):
        flag = True
        while flag:
            choice = int(input(self.menu))
            if choice == '1':
                self.main.add_note()
                continue
            elif choice == '2':
                self.main.read_notes()
                continue
            elif choice == '3':
                input_date = input(self.input_date)
                self.main.get_by_date(input(f"Notes by date {input_date}: \n"))
                continue
            elif choice == '4':
                self.main.read_notes()
                input_note = int(input(self.input_id))
                if self.main.print_by_id(input_note) == True:
                    self.main.delete_note(input_note)
                    continue
                else:
                    continue
            elif choice == '5':
                flag2 = True
                self.main.read_notes()
                input_note = int(input(self.input_id))
                if (self.main.print_by_id(input_note) == True):
                    while flag2:
                        change_choice = int(input(self.menu_change))
                        if change_choice == 1:
                            new_title = input(self.new_text)
                            self.main.change_title(input_note, new_title)
                            continue
                        if change_choice == 2:
                            new_title = input(self.new_text)
                            self.main.change_body(input_note, new_title)
                            continue
                        elif change_choice == 3:
                            flag2 = False
            if choice == '0':
                flag = False
