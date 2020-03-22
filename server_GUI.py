from tkinter import *

root = Tk()
root.geometry('1000x600')
root.resizable(0, 0)
root.title('')

# dictionary of all people and the positions of them
people_pos = {}
# positions of all the buttons
button_pos = {}


def add_button(x, y):
    the_button = Button(root, text='+', bg='white', width=5, height=2, command=add_click)
    the_button.config(font=('courier', 10, "bold"))
    the_button.place(x=x, y=y)


class Popup:
    def __init__(self, self_root):
        self.root = self_root

    def create_popup(self):

        def clicked():
            p = Person(name.get(), jobs.get().split(','))
            print(jobs.get().split(','))
            p.create_person()

        win = Toplevel(self.root)
        win.geometry('200x210')
        win.resizable(0, 0)

        name_label = Label(win, text='Name', bg='light gray')
        name_label.config(font=('Courier', 20, 'bold'))
        name_label.place(x=55, y=5)

        name = Entry(win, width=25)
        name.place(x=0, y=40)

        jobs_label = Label(win, text='Jobs', font=('courier', 20, 'bold'), bg='light gray')
        jobs_label.place(x=55, y=65)

        jobs = Entry(win, width=25)
        jobs.place(x=0, y=100)

        submit = Button(win, text='Submit', command=clicked)
        submit.place(x=65, y=150)

        win.attributes('-topmost', 'true')

        win.config(bg='light gray')

        win.mainloop()


def add_click():
    up = Popup(root)
    up.create_popup()


class CreateButton:
    def __init__(self, x, y, text):
        # X position of the button
        self.x = x

        # Y position of the button
        self.y = y

        # Text of the button
        self.text = text

        # Creates the button
        self.b = Button(root, text=self.text, width=15, height=3, command=self.click, bg='red')

    # Function executes when the button clicks
    # Changes the color of the button
    def click(self):
        # If background is red, turn it green
        if self.b.cget('bg') == 'red':
            self.b.config(bg='green')
        # Else set is green
        else:
            self.b.config(bg='red')

    # Adds the button to the window
    def create(self):
        self.b.place(x=self.x, y=self.y)


class Person:
    def __init__(self, person, *args):
        # Sets the person
        self.person = person
        # this creates a list of all the args given
        self.args = args
        print(list(self.args))

    def create_person(self):
        # This creates the first person on the list
        if len(people_pos) == 0:

            # Creates the name label
            t = Label(root, text=str(self.person), bg='white')

            # Configures the font and size of the label then places it
            t.config(font=('courier', 30))
            t.place(x=0, y=85)

            # Creates the horizontal line under each name and job
            can.create_line(0, 155, 1000, 155, fill='light gray', width=5)

            # Adds the person and position to the list
            people_pos[0] = 145
            print(people_pos)

            for i in range(len(self.args[0])):
                b = CreateButton(253 + i * 135, 75, self.args[0][i])
                b.create()

        else:
            # Returns the last key of the dictionary
            last_key = list(people_pos.keys())[-1]

            # Returns the last value using the key found above
            last_value = people_pos.get(last_key)

            # Creates Label
            t = Label(root, text=str(self.person), bg='white')
            t.config(font=('courier', 30))
            t.place(x=0, y=last_value + 25)
            # ---------------------------------------------------

            can.create_line(0, last_value + 93, 1000, last_value + 93, fill='light gray', width=5)
            people_pos[len(people_pos)] = last_value + 85

            for x in range(len(self.args[0])):
                b = CreateButton(253 + x * 135, last_value + 15, self.args[0][x])
                b.create()


root.iconbitmap('favicon.ico')

can = Canvas(root, bg='white', height=600, width=1000)
can.place(x=0, y=0)

can.create_line(0, 70, 1000, 70, fill='light gray', width=5)
can.create_line(250, 0, 250, 600, fill='light gray', width=5)

people = Label(root, text='People', bg='white', fg='blue')
people.config(font=('Courier', 30))
people.place(x=30, y=5)

jobs = Label(root, text='Jobs', bg='white', fg='red')
jobs.config(font=('courier', 30))
jobs.place(x=550, y=5)

add_button(930, 7)


print(people_pos)


root.mainloop()
