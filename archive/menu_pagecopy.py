from tkinter import filedialog
from tkinter import *
from menu_page import *

import tkinter as tk
from tkinter import filedialog, font
from tkinter.messagebox import showerror

from cv_uploader2 import MyWindow


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        """Initialise the main app"""
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # Here we will build a container but only make the selected one visible
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # NP - do you understand what this for loop does and where it's used
        self.frames = {}
        for F in (StartPage, CVUploader, CallBooker, MyWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Put all of the pages in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """ Show a frame for the given page name """
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # NP - separate functionality for ease of understanding. Naming very important.
        self.create_header()
        self.create_menu()

    def create_header(self):
        label = tk.Label(self, text="Recruitment Platform", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)

    def create_menu(self):
        button1 = self.create_frame_button("Upload Your CV", "CVUploader")
        button1.pack()
        button2 = self.create_frame_button("Book In A Call", "CallBooker")
        button2.pack()
        button3 = self.create_frame_button("CV Uploader 2", "MyWindow")
        button3.pack()

    def create_frame_button(self, text, frame_name):
        return tk.Button(self, text=text, command=lambda: self.controller.show_frame(frame_name))


# NP - Read the docstring. Do you understand Python classes and subclassing? Use to apply a common theme as required.
#    - Can apply to StartPage if you like too. Consider using a conditional such as `if self.__name__ != "StartPage"`
#      to create footer or not
class BaseSubPage(tk.Frame):
    """ Basic framework for sub pages

    Creates header and footer, page_content must be implemented
    """
    page_title = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.create_header()
        self.page_content()
        self.create_footer()

    def create_header(self):
        """ Creates page header """
        if self.page_title is None:
            # NP - throw errors when human errors/mistakes can be introduced
            raise TypeError(f"page_title must be str type, not {type(self.page_title)}")
        page_title = tk.Label(self, text=self.page_title, font=self.controller.title_font)
        page_title.pack(side="top", fill="x", pady=10)

    def page_content(self):
        """ Must be implemented in subclass """
        # NP - ensures that you implement something
        raise NotImplementedError

    def create_footer(self):
        """ Create page footer """
        button = tk.Button(self, text="Back to the start page",
                           command=lambda: self.controller.show_frame("StartPage"))
        button.pack()


class CVUploader(BaseSubPage):

    def __init__(self, parent, controller):
        self.page_title = "CV Uploader"
        super().__init__(parent, controller)

        # NP - left in so you can see that it's missing
        #tk.Frame.__init__(self, parent)
        #self.controller = controller
        #label = tk.Label(self, text="CV Uploader", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)

        #button = tk.Button(self, text="Back to the start page",
                            #command=lambda: controller.show_frame("StartPage"))
        #button.pack()

    def page_content(self):
        upload_button = tk.Button(self, text="Select file", command=self.upload_action)
        upload_button.pack()

    def upload_action(self):
        """ Handles file upload """
        filename = filedialog.askopenfilename()
        print('Selected:', filename)

        if filename:
            try:
                print(f"Now do something with {filename}")
                raise TypeError  # NP - so you can see the try/except block
            except TypeError as err:  # NP - add the exception handling that you need
                showerror(f"Failed to read file {filename} with error: {err}")

class CallBooker(BaseSubPage):

    def __init__(self, parent, controller):
        self.page_title = "Call Booker"
        super().__init__(parent, controller)
        # tk.Frame.__init__(self, parent)
        # self.controller = controller
        # label = tk.Label(self, text="Call Booker", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        # button = tk.Button(self, text="Back to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()

    # NP - will run when you uncomment this
    def page_content(self):
        pass  # shows intent to not implement method


if __name__ == "__main__":
    app = MainApp()
    app.geometry("700x800+10+10")
    app.mainloop()