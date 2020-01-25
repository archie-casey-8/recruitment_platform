import tkinter as tk

from tkinter import filedialog

from tkinter import *





class MyWindow(tk.Frame):  # NP - Better naming

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller



        self.first_name=Label(self, text = 'First Name')

        self.last_name=Label(self, text = 'Last Name')

        self.phone_num=Label(self, text = 'Mobile Number')

        self.more_info=Label(self, text = 'Any other info you feel is applicable')

        self.f_n = Entry(self, width= '20', bd = '4')

        self.l_n = Entry(self, width= '20', bd = '4')

        self.p_n = Entry(self, width= '20', bd = '4')

        self.m_i = Text(self, width= '50', bd = '4', height = '4')

        self.first_name.place(x = 50, y = 50)

        self.f_n.place(x=150, y = 50)

        self.last_name.place(x = 50, y= 100)

        self.l_n.place(x = 150,y = 100)

        self.phone_num.place(x = 50, y = 150)

        self.p_n.place(x = 150,y = 150)

        self.more_info.place(x = 50 ,y = 200)

        self.m_i.place(x = 50 ,y = 230)

        self.open = Button(self, text='Open', width = '7', height = '1', bd = '3', command= self.UploadAction)

        self.upload = Button(self, text = 'Upload', width = '7', height = '1', bd = '3')

        self.home = Button(self, text = 'Return back to\n home screen', width = '13',

                           height = '2',activebackground = 'black', activeforeground = 'red',

                           bd = '3', relief = 'raised', command=lambda: self.controller.show_frame("StartPage"))

        # self.exit = Button(self, text = 'EXIT', width = '8', height = '2',activebackground = 'black', activeforeground = 'red', bd = '10', relief = 'raised', command= window.destroy)

        self.open.place(x= 50, y= 600)

        self.upload.place(x= 200, y= 600)

        self.home.place(x= 300, y= 600)

        # self.exit.place(x= 500, y= 600)



    def UploadAction(event=None):

        filename = filedialog.askopenfilename()

        print('Selected:', filename)



    def read_from_file(self):

        '''Read csv file and return a list like: [[username, password, count]]'''

        try:

            with open(CSV_FILE, 'rb') as f:

                users = []

                reader = csv.reader(f)

            for row in reader:

                row[2] = int(row[2]) # Make the count an integer so it can increase later

                users.append(row)

                return users

        except IOError:

            popup("Error", "File not found!")





# window = Tk()

# mywin = MyWindow(window)

# window.title("Hello Python")

# window.geometry("700x800+10+10")

# window.mainloop()
