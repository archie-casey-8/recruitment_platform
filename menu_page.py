from tkinter import filedialog
from tkinter import *

def menu():
    class MyWindow:
        def __init__(self, win):
            self.first_name=Label(win, text = 'First Name')
            self.first_name.place(x = 50, y = 50)



window = Tk()
mywin = MyWindow(window)
window.title("Hello Python")
window.geometry("700x800+10+10")
window.mainloop()
