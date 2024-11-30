from tkinter import *
from tkinter import messagebox
import customtkinter
import mysql.connector
from datetime import date, datetime

# Global Variables
now = datetime.now()
tasklst = []

# Connecting to the database
def database_connection():
    global mydb, cursor
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="todo_task"
    )
    cursor = mydb.cursor()
    if mydb.is_connected():
        print("Connected to MySQL Database.....")
    else:
        messagebox.showerror("Server Error", "Unable to connect to server")
        window.destroy()

def ensure_connection():
    if not mydb.is_connected():
        database_connection()

# Load tasks from the database on startup
def load_tasks():
    ensure_connection()
    cursor.execute("SELECT task_name FROM task")
    tasks = cursor.fetchall()  # Fetch all tasks
    for task_tuple in tasks:
        task = task_tuple[0]  # Get task name from tuple
        tasklst.append(task)
        custom_checkbox(task)  # Display each task as a checkbox

# Add task to the database and list
def add_task():
    ensure_connection()
    task = taskEntry.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Task cannot be empty.")
    else:
        sql = "INSERT INTO task (task_name, task_time, task_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (task, now.strftime("%H:%M:%S"), date.today()))
        mydb.commit()
        print("Task added successfully.")
        tasklst.append(task)
        custom_checkbox(task)  # Display the newly added task

# Function to handle checkbox check and delete task
def on_task_checked(event, task, frame2):
    ensure_connection()
    sql = "DELETE FROM task WHERE task_name = %s"
    cursor.execute(sql, (task,))
    mydb.commit()
    print(f"Task '{task}' deleted successfully.")
    tasklst.remove(task)
    frame2.destroy()  # Remove the task's frame from the UI

# Creating checkboxes for tasks
def custom_checkbox(task):
    frame2 = customtkinter.CTkFrame(master=window, corner_radius=0, fg_color="transparent")
    frame2.pack(anchor='w', fill='both', side="top", padx=10, pady=5)
    
    check_btn = customtkinter.CTkCheckBox(frame2, text=task, font=("inter", 12))
    check_btn.pack(anchor='w')
    check_btn.bind("<ButtonRelease-1>", lambda event, task=task, frame=frame2: on_task_checked(event, task, frame2))

    taskEntry.delete(0, END)

# Creating main window
window = customtkinter.CTk()
window.geometry("900x600")
sbb = Scrollbar(window)
sbb.pack(side='right', fill=Y)
window.title("ToDo App")
customtkinter.set_appearance_mode("light")

# Input Frame
InputFrame = customtkinter.CTkFrame(master=window, fg_color="Light Grey", height=130, corner_radius=0)
InputFrame.pack(fill='both', side="top", anchor='w')

addtsk = customtkinter.CTkLabel(InputFrame, text="Add Task", font=("Inter", 16), fg_color=None)
addtsk.pack(padx=10, pady=4, anchor='w')

taskEntry = customtkinter.CTkEntry(InputFrame, width=300, corner_radius=8, border_color="light blue")
taskEntry.pack(padx=10, pady=4, anchor='w')

addbtn = customtkinter.CTkButton(
    InputFrame,
    text="Add task",
    width=140,
    height=30,
    corner_radius=6,
    command=add_task,
    border_spacing=10,
    font=("inter", 14)
)
addbtn.pack(padx=10, pady=4, anchor='w')

database_connection()  # Connect to the database
load_tasks()  # Load tasks from the database when the app starts
window.mainloop()



