from tkinter import *

class Popup:
    def __init__(self, root):
        self.root = root

    def create_popup(self):
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

        submit = Button(win, text='Submit')
        submit.place(x=65, y=150)

        win.attributes('-topmost', 'true')

        win.config(bg='light gray')

        win.mainloop()
