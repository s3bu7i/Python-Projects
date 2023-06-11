from tkinter import *
root = Tk()
root.geometry("400x300")

def get_number():
    n1 = int(entry1.get()) # 3
    n2 = int(entry2.get()) # 5
    n3 = int(entry3.get()) 
    n4 = int(entry4.get())
    n5 = int(entry5.get())
    lst = [n1, n2, n3, n4,n5]

    addition = 0 
    for i in lst:
        addition += i
    Label(root, text="Addition = "+str(addition)).pack()

    product = 1
    for i in lst:
        product *= i
    Label(root, text="Product = "+str(product)).pack()


entry1 = Entry(root, width=40)
entry1.pack(pady=4)
entry2 = Entry(root, width=40)
entry2.pack(pady=4)
entry3 = Entry(root, width=40)
entry3.pack(pady=4)
entry4 = Entry(root, width=40)
entry4.pack(pady=4)
entry5 = Entry(root, width=40)
entry5.pack(pady=4)
btn = Button(root, text="Enter", command=get_number)
btn.pack()
root.mainloop()
