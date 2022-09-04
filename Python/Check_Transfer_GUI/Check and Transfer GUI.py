#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.10
#
# Author:       H. Shultz
#
# Purpose:    TA - Python course: a user interface that allows the user 
#             to browse and select a specific folder that will contain daily 
#             files, and a specific folder that will receive the copied files. 
#             It also allows the user to manually initiate a 'file check' process 
#             that will check for any new/modified files in the last 24 hours 
#             and copy them to the destination folder.  
#
# Tested OS:  This code was written and tested to work with Windows 11.

#to display directory selector 
from distutils.fancy_getopt import wrap_text
from fileinput import filename

#for widget window
from tkinter import filedialog
from tkinter import *
import tkinter as tk

#allows manipulation of files 
from re import I
import shutil

#to retrieve current time & last modification time of files 
import os, datetime
import time


#window created
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # define our master frame configuration
        self.master = master
        self.master.minsize(350,200) #(Width,Height)
        self.master.maxsize(350,200)
        self.master.title("Daily Sync")
        self.master.configure(bg="#F0F0F0")

        #create source folder label
        self.lbl_source = tk.Label(self.master,text='Folder to upload from:')
        self.lbl_source.grid(row=0,column=0,padx=(5,0),pady=(5,0),sticky=N+W)
        #create source folder Entry box which is filled when user selects directory
        self.source_entry = tk.Entry(self.master,'',width=40)
        self.source_entry.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(10,0),pady=(0,0),sticky=N+E)
        #create source folder browse button 
        self.btn_source = tk.Button(text="Browse", command=lambda:source_button(self,''))
        self.btn_source.grid(row=1, column=3,padx=(10,0),pady=(10,0),sticky=N+E)
        #create destination folder label
        self.lbl_destination = tk.Label(self.master,text='Folder to upload to:')
        self.lbl_destination.grid(row=2,column=0,padx=(5,0),pady=(5,0),sticky=N+W)
        #create destination folder Entry box which is filled when user selects directory
        self.destination_entry = tk.Entry(self.master,'',width=40)
        self.destination_entry.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(10,0),pady=(0,0),sticky=N+E)
        #create destination folder browse button
        self.btn_destination = tk.Button(text="Browse", command=lambda:des_button(self,''))
        self.btn_destination.grid(row=3, column=3,padx=(10,0),pady=(10,0),sticky=N+E)
        #create start transfer button 
        self.btn_transfer = tk.Button(text="Start Transfer", command=lambda:file_check(self))
        self.btn_transfer.grid(row=4, column=1,columnspan=2,padx=(10,0),pady=(10,0),sticky=N+E)


#when button is clicked
def source_button(self,s_filename):
    #prove a directory browser for user to select path
    s_filename = filedialog.askdirectory()
    #deletes anything in entry field 
    self.source_entry.delete(0,END)
    #sets user selected path into entry field
    self.source_entry.insert(0,s_filename)

def des_button(self,d_filename):
    d_filename = filedialog.askdirectory()
    self.destination_entry.delete(0,END)
    self.destination_entry.insert(0,d_filename)

def file_check(self):
    #set user selected source path
    source = self.source_entry.get()
    #set the user selected destination path
    destination = self.destination_entry
    #retrieves list of all files in source
    files = os.listdir(source)
    for file in files:
        if file.endswith('.txt'):
            #subtracts the current time from the time the files was last modified 
            chk_time = time.time() - os.path.getmtime(source + file)
            # coverts seconds to hours and checks if it is less that 24
            if chk_time / 3600 < 24:
                #we are saying move the files represented by 'files' to their new destination 
                shutil.copy(source + file, destination)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
