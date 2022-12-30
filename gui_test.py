from tkinter import *

root = Tk()
root.title('Test - Drop down menu')
root.geometry("400x400")


data = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

clicked = StringVar()
clicked.set("empty")

# dropdown box
drop = OptionMenu(root, clicked, *data)
drop.pack()

def Show():
    print(clicked.get())
button = Button(root, command=Show, text= "Show").pack()

root.mainloop()
