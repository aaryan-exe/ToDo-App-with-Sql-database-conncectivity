from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Button, Label, PhotoImage, Frame
import os
import mysql.connector
import datetime

global window
global task
#Connecting database
# def database_connection():
#     mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="system",
#     database="ToDo_task"
# )
#     if mydb.is_connected:
#         print("Connected to MySQL Database.....")
#     else:
#         messagebox.ERROR("server error", "Unable to connct to server")
#         window.destroy


#Add task button function
def add_task():
    task=taskEntry.get()
    if task.strip()=="":
        messagebox.showwarning("Input error", "Wrong input")
    else:
        custom_checkbox()


def custom_checkbox(window):
    img = PhotoImage(file="images/custom_checkbox.png")
    uncheck_button = Button(window, image=img)
    uncheck_button.img=img
    uncheck_button.pack
    
    

#Creating main window
window=Tk()
window.geometry("900x600")
addtsk=Label(window, text="Add task", font=("inter", 16)).place(x=20, y=20)
taskEntry=Entry(window, width=40)
taskEntry.place(x=20, y=55)
addbtn=Button(window, text="Add task", command=add_task, font=("inter", 11)).place(x=20, y=80)




# database_connection() #connecting database function
window.mainloop()