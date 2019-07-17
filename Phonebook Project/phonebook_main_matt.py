#Python Ver: 3.7.1
#
#Author: Matt Kunnari
#
#Purpose: Phonebook Demo, demonstrating OOP, Tkinter GUI, Parent Child Relationships, Sqlite3
#
#
#Tested OS: Code tested to work on Windows 10
#Written: 7/12/2019

from tkinter import *
import tkinter as tk


#Gives access to the other modules related to this program
import phonebook_gui_matt
import phonebook_func_matt


#Frame is the Tkinter fram class that our own class will inherit
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self,master,*args,**kwargs)

        #define our master frame config
        self.master = master
        self.master.minsize(500,300)#(height,width)
        self.master.maxsize(500,300)
        #this will center our window on the users screen
        phonebook_func_matt.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg='#F0F0F0')
        #this protocol method is a tkinter built in method to catch is
        #the user clicks the upper corner x on windows OS
        self.master.protocol("WM_DELETE_WINDOW",lambda: phonebook_func_matt.ask_quit(self))
        arg=self.master

        #load in the GUI widgets from a seperate module,
        #keeping the code compartmentalized and clutter free
        phonebook_gui_matt.load_gui(self)


if__name__ = "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
