import re
from tkinter import *
root = Tk()
root.geometry("400x300")

def get_username():
    u_name = entry.get()
    x = re.search("[a-zA-Z]+[0-9]+",u_name)
    if x:
        print("Username correct, because it contian alphanumeric char")
        Label(root, text="Username correct, because it contian alphanumeric char").pack()
    else:
        print("Not correct, include alphanumeric char")
        Label(root, text="Not correct, include alphanumeric char").pack()
entry = Entry(root, width=40)
entry.pack(pady=4)

btn = Button(root, text="Enter", command=get_username)
btn.pack()
root.mainloop()
