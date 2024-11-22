from tkinter import *
from tkinter import messagebox
import customtkinter
import os
import mysql.connector
import datetime

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


#Add task button function
def add_task():
    task=taskEntry.get()
    if task.strip()=="":
        messagebox.showwarning("Input error", "Wrong input")
    else:
        custom_checkbox()

def custom_checkbox():
    frame2=customtkinter.CTkFrame(master=window, fg_color="black", height=50, corner_radius=0)
    frame2.pack(anchor ='w', fill='both',side="top")
    task1=Label(frame2,text='task',font=("inter", 11), background="white")
    task1.pack(anchor='w', padx=10)

#Creating main window
window=customtkinter.CTk()
window.geometry("900x600")
# window.resizable(False, False)
window.title("ToDo App")
customtkinter.set_appearance_mode("light")

InputFrame=customtkinter.CTkFrame(master=window, fg_color="Light Grey", height=130, corner_radius=0)
InputFrame.pack(fill='both', side="top", anchor='w')

addtsk = customtkinter.CTkLabel(InputFrame, text="Add Task", font=("Inter", 16), fg_color=None)
addtsk.pack(padx=10,pady=10, anchor='w')

taskEntry=customtkinter.CTkEntry(InputFrame, width=300)
taskEntry.pack(padx=10,pady=10, anchor='w')

addbtn=customtkinter.CTkButton(InputFrame, text="Add task", command=add_task, font=("inter", 11))
addbtn.pack(padx=10,pady=10, anchor='w')



# database_connection() #connecting database function
window.mainloop()