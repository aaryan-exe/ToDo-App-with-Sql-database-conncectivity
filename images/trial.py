from tkinter import Tk, Button, Label

root = Tk()
label = Label(root, text="Click here:")
label.pack(side="left", padx=5)
button = Button(root, text="Submit")
button.pack(side="left", padx=5)
root.mainloop()
