

from tkinter import *
import time


win =   Tk()
win.title("Digital clock")
win.geometry("300x150")

def digital_clock():
    time1 = time.strftime("%H:%M:%S")
    current_time.config(text = time1)
    current.time.after(250,digital_clock())
    
digital_clock = Label(win,font = ("times new roman",35,"bold"),bg = "red")
digital_clock.grid(row = 0,column = 0)

current_time = Label(win,font = ("times new roman",35,"bold"),bg = "red")
current_time.grid(row =0, column =0, padx=60,pady=30)

digital_clock()

win.mainloop()
COMMAND
    
