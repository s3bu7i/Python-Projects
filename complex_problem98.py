from collections import UserString
from re import L
from tkinter import *
root = Tk()
root.geometry("400x300")

def get_str():
    user_str = entry.get()
    flg = "no"
    for i in user_str:
        if i.isspace():
            flg = "yes"
            
    if flg == "yes":
        Label(root, text="String have space").pack()
    else:
        Label(root, text="String have no space").pack()

entry = Entry(root, width=40)
entry.pack(pady=4)

btn = Button(root, text="Enter", command=get_str)
btn.pack()
root.mainloop()
