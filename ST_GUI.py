import tkinter as TK
from tkinter import *
import db_interface

class MainWindow(): # blueprint for the gui
    def __init__(self, master):
        self.master = master
        # size for gui
        self.master.geometry("200x280")

        # make title for the GUI
        #                     name of gui, title
        self.lbl_title = TK.Label(master, text="Title")
        # placing the title above at (x,y) coordinates
        self.lbl_title.place(x=10,y=10)
        
        # Item names tab
        self.lbl_item_name1 = TK.Label(master, text="Item Name")
        self.lbl_item_name1.place(x=10,y=50)
        # drop down menu for item name
        items = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]
        self.drop_item_name1 = StringVar()
        self.drop_item_name1.set("Select Item!")
        # dropdown
        options = OptionMenu(master, self.drop_item_name1, *items)
        options.pack()
        #self.item1=None
        #def set():
        #    item1=drop_item_name1.get()
        #button_drop = Button(root, command=set, text="Click to Confirm").pack()
        
        # adding new label
        self.lbl_item_name2 = TK.Label(master, text="Buy Price")
        self.lbl_item_name2.place(x=10,y=90)

        # PUTTING TEXT FIELD
        self.txt_item_name2 = TK.Entry(master)
        self.txt_item_name2.place(x=10,y=110)

        # adding new label
        self.lbl_item_name3 = TK.Label(master, text="Sell Price")
        self.lbl_item_name3.place(x=10,y=130)

        # PUTTING TEXT FIELD
        self.txt_item_name3 = TK.Entry(master)
        self.txt_item_name3.place(x=10,y=150)

        # adding new label
        self.lbl_item_name4 = TK.Label(master, text="Quantity")
        self.lbl_item_name4.place(x=10,y=170)

        # PUTTING TEXT FIELD
        self.txt_item_name4 = TK.Entry(master)
        self.txt_item_name4.place(x=10,y=190)


        # button
        self.btn_submit = TK.Button(master, text = "Submit", command = self.submit_to_db)
        self.btn_submit.place(x=10,y=230)

    def submit_to_db(self):
        item_name = self.drop_item_name1.get()
        # gives error when item is not selected
        #if item_name == "Select Item!":
        #    return -1
        buy_price = int(self.txt_item_name2.get())
        sell_price = int(self.txt_item_name3.get())
        quantity = int(self.txt_item_name4.get())
        db_interface.write_to_database(item_name, buy_price, sell_price, quantity)
# launchin GUI
root = TK.Tk() # this is master
my_gui = MainWindow(root)
# kick off the GUI makes it appear on screen
root.mainloop()