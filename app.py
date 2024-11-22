from tkinter import *
from tkinter import messagebox
import os
import mysql.connector

global window
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

#Creating main window
window=Tk()
window.geometry("900x600")
addtsk=Label(window, text="Add task", font=("inter", 16)).place(x=20, y=20)
addtsk_entry=Entry(window, width=40).place(x=20, y=55)
addbtn=Button(window, text="Add task", command=None, font=("inter", 11)).place(x=20, y=80)




# database_connection() #connecting database function
window.mainloop()