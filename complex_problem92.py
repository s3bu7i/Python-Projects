from tkinter import *
root = Tk()
root.geometry("400x300")

def get_value():
    marks =  int(entry.get())
    if marks >=95:
        Label(root, text="Your grade is A+").pack()
    elif marks >=80:
        Label(root, text="Your grade is A").pack()
    elif marks >=70:
        Label(root, text="Your grade is B").pack()
    elif marks >=60:
        Label(root, text="Your grade is C").pack()
    else:
        Label(root, text="Your are fail").pack()

entry = Entry(root, width=40)
entry.pack()
btn = Button(root, text="Get Grade", command=get_value)
btn.pack()
root.mainloop()
