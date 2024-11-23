from tkinter import *
from tkinter import messagebox
import customtkinter
import mysql.connector
from datetime import date, datetime

global window
global task
now = datetime.now()
tasklst=[]
#Connecting database
def database_connection():
    global mydb, cursor
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="system",
    database="todo_task"
)
    cursor=mydb.cursor()
    if mydb.is_connected():
        print("Connected to MySQL Database.....")
    else:
        messagebox.showerror("server error", "Unable to connct to server")
        window.destroy

def ensure_connection():
    if not mydb.is_connected():
        database_connection()

#Add task button function
def add_task():
    ensure_connection()
    task=taskEntry.get()
    if task.strip()=="":
        messagebox.showwarning("Input Error", "Task cannot be empty.")
    else:
        sql="INSERT INTO task (task_name, task_time, task_date) VALUES (%s, %s, %s)"
        cursor.execute(sql,(task, now.strftime("%H:%M:%S"), date.today()))
        mydb.commit()
        print("Task added successfully.")
        tasklst.append(task)
        custom_checkbox(task)



#creating checkboxes
def custom_checkbox(task):
    frame2=customtkinter.CTkFrame(master=window,corner_radius=0, fg_color="transparent")
    frame2.pack(anchor ='w', fill='both',side="top", padx=10, pady=5)
    task1=Label(frame2,font=("inter", 11))
    task1.pack(anchor='w')
    uncheck_btn=customtkinter.CTkCheckBox(frame2, text=task, font=("inter", 12))
    uncheck_btn.pack(anchor='w')
    taskEntry.delete(0, END)
    print(uncheck_btn.get())
    
    


#Creating main window
window=customtkinter.CTk()
window.geometry("900x600")
sbb=Scrollbar(window)
sbb.pack(side='right', fill=Y)
window.title("ToDo App")
customtkinter.set_appearance_mode("light")

InputFrame=customtkinter.CTkFrame(master=window, fg_color="Light Grey", height=130, corner_radius=0)
InputFrame.pack(fill='both', side="top", anchor='w')

addtsk = customtkinter.CTkLabel(InputFrame, text="Add Task", font=("Inter", 16), fg_color=None)
addtsk.pack(padx=10,pady=4, anchor='w')

taskEntry=customtkinter.CTkEntry(InputFrame, width=300, corner_radius=8, border_color="light blue")
taskEntry.pack(padx=10,pady=4, anchor='w')

addbtn=customtkinter.CTkButton(InputFrame,
 text="Add task", 
 width=140, 
 height=30, 
 corner_radius=6, 
 command=add_task, 
 border_spacing=10,
 font=("inter", 14))
addbtn.pack(padx=10,pady=4, anchor='w')



database_connection() #connecting database function
window.mainloop()