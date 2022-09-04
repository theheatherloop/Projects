#
# Python:    3.10
#
# Author:    H.Shultz
#
# Purpose:   TTA - Python Course, Create a GUI that allows the user to input text, 
#            generates a web page that sets the user’s input as the body text for the web page,
#            and opens the generated web page in the browser. 
#


# importing webbrowser module
import os
import webbrowser
# importing all files from tkinter module
from tkinter import * 
# importing messagebox from tkinter module
from tkinter import messagebox
import tkinter as tk
from tkinter.messagebox import askokcancel


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #  define our ParentWindow (master) frame configuration
        self.master = master
        self.master.title("Web Page Generator")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master

        self.lbl_info = tk.Label(self.master,text='Enter text for Website below:')
        self.lbl_info.grid(row=0,column=0,padx=(5,0),pady=(10,0))

        self.txt_web = tk.Text(self.master,wrap=WORD,width=40,height=10,)
        self.txt_web.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,30),pady=(10,10))

        self.btn_create = tk.Button(self.master,width=12,height=2,text='Create Page',command=lambda: createPage(self))
        self.btn_create.grid(row=2,column=0,padx=(40,150),pady=(0,10))

        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: ask_quit(self))
        self.btn_close.grid(row=2,column=0,padx=(200,0),pady=(0,10))

    
        def createPage(self):
            userInput = self.txt_web.get("1.0",'end')
            all = ('''<html>\n,<body>\n'''+ userInput + "\n" + '''</body>\n, </html>''')
            #opens our html file
            file = open("basic_html.html", "w")
            #replace our html file with our new input
            file.writelines(all)
            webbrowser.open("basic_html.html", new=2, autoraise=True)
    

        # catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
        def ask_quit(self):
            if tk.messagebox.askokcancel("Exit program", "Okay to exit application?"):
                # This closes app
                self.master.destroy()
                os._exit(0)

if __name__ == "__main__":
    #This Instantiates the Tk.() root frame (window) into being
    root = tk.Tk()
    #This instantiates our own class as an App object
    App = ParentWindow(root)
    #This ensures the Tkinter class object, our window, will keep looping
    root.mainloop()
