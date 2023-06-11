from tkinter import *
root = Tk()
root.geometry("400x300")

def get_colors():
    color1 = entry1.get()
    color2 = entry2.get()
    color3 = entry3.get()
    color4 = entry4.get()
    color5 = entry5.get()
    lst = [color1, color2, color3, color4,color5]
    for i in lst:
        list_items = i +" having length of "+str(len(i)+" char")
        Label(root, text=list_items).pack()

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
btn = Button(root, text="Enter", command=get_colors)
btn.pack()
root.mainloop()
