from tkinter import *

root = Tk()
root.geometry("400x300")

def get_value():
    num =  int(entry.get())
    if num%2 == 0 and num%3 == 0:
        Label(root, text="Number is divisible by 2 and 3").pack()
    else:
        Label(root, text="Not").pack()
entry = Entry(root, width=40)
entry.pack()
btn = Button(root, text="Enter", command=get_value)
btn.pack()
root.mainloop()
