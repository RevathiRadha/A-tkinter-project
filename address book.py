#============================================= ADDRESS BOOK ==============================================================================================================

#---------------------------------------------- PYTHON PROJECT -----------------------------------------------------------------------------------------------------------

#``````````````````````````````````````````````` R.REVATHI `````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#=============================================== IMPORT MODULES ==========================================================================================================

from tkinter import *
import sqlite3
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

#-----------------------------------------------------------MAIN WINDOW-------------------------------------------------------------------------------------------------------------

root = Tk()
root.geometry('1000x600')
root.title("Address Book")
root.iconbitmap('D:\\Address_Book\\icon\\address-book.ico')
root.config(bg = 'powderblue')

#============================================= VARIABLES =================================================================================================================

NAME = StringVar()
AGE = StringVar()
GENDER = StringVar()
TELEPHONE = StringVar()
MOBILE = StringVar()
OFFICE = StringVar()
EMAIL = StringVar()
ADDRESS = StringVar()
RELATION = StringVar()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Database():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `address_book` (S_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE TEXT NOT NULL, GENDER TEXT NOT NULL, TELEPHONE TEXT NOT NULL, MOBILE TEXT NOT NULL, OFFICE TEXT NOT NULL, EMAIL VARCHAR(20) NOT NULL, ADDRESS TEXT NOT NULL, RELATION TEXT NOT NULL)")
    cursor.execute("SELECT * FROM `address_book` ORDER BY `NAME` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        table.insert('', 'end', values = (data))
    cursor.close()
    conn.close()
        
#----------------------------------------------------CANCEL------------------------------------------------------------------------------------------------------------------------------ 

def add_cancel():
    AddContact.destroy()

def edit_cancel():
    EditContact.destroy()
    
#-----------------------------------------------------DELETE---------------------------------------------------------------------------------------------------------------------------- 

def delete():
    if not table.selection():
       result = messagebox.showwarning('Delete Contact', 'Please Select the contact to delete', icon="warning")
    else:
        result = messagebox.askquestion('Delete Contact', 'Are you sure you want to delete this contact?', icon="warning")
        if result == 'yes':
            cursor_item = table.focus()
            contents =(table.item(cursor_item))
            selected_item = contents['values']
            table.delete(cursor_item)
            conn = sqlite3.connect("address_book.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `address_book` WHERE `S_No` = %d" % selected_item[0])
            conn.commit()
            cursor.close()
            conn.close()

#-------------------------------------------------------- SAVE -------------------------------------------------------------------------------------------------------------------------- 

def save():

    if NAME.get() == "" or AGE.get() == "" or GENDER.get() == "" or MOBILE.get() == "" or EMAIL.get() == "" or ADDRESS.get() == "" or RELATION.get() == "":
        result = messagebox.showwarning('Data Missing', 'Please Complete Required Fields', icon = 'warning')

    else:
        table.delete(* table.get_children())

        conn = sqlite3.connect("address_book.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `address_book` (NAME, AGE, GENDER, TELEPHONE, MOBILE, OFFICE, EMAIL, ADDRESS, RELATION) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(NAME.get()), int(AGE.get()), str(GENDER.get()), str(TELEPHONE.get()), str(MOBILE.get()), str(OFFICE.get()), str(EMAIL.get()), str(ADDRESS.get()), str(RELATION.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `address_book` ORDER BY `NAME` ASC")
        fetch = cursor.fetchall()

        for data in fetch:
            table.insert('', 'end', values = (data))
        cursor.close()
        conn.close()

        NAME.set("")
        AGE.set("")
        GENDER.set("")
        TELEPHONE.set("")
        MOBILE.set("")
        OFFICE.set("")
        EMAIL.set("")
        ADDRESS.set("")
        RELATION.set("")
    

#----------------------------------------------------- EDIT ------------------------------------------------------------------------------------------------------------------------ 

def edit():

    if NAME.get() == "" or AGE.get() == "" or GENDER.get() == "" or MOBILE.get() == "" or EMAIL.get() == "" or ADDRESS.get() == "" or RELATION.get() == "":
        result = messagebox.showwarning('Data Missing', 'Please Complete Required Fields', icon = 'warning')

    else:
        table.delete(* table.get_children())

        conn = sqlite3.connect("address_book.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `address_book` SET `NAME` = ?, `AGE` = ?, `GENDER` = ?, `TELEPHONE` = ?, `MOBILE` = ?, `OFFICE` = ?,`EMAIL` = ?, `ADDRESS` = ?, `RELATION` = ? WHERE `S_No` = ?", (str(NAME.get()), int(AGE.get()), str(GENDER.get()), str(TELEPHONE.get()), str(MOBILE.get()), str(OFFICE.get()), str(EMAIL.get()), str(ADDRESS.get()), str(RELATION.get()), int(S_No)))
        conn.commit()
        cursor.execute("SELECT * FROM `address_book` ORDER BY `NAME` ASC")
        fetch = cursor.fetchall()

        for data in fetch:
            table.insert('', 'end', values = (data))
        cursor.close()
        conn.close()

        NAME.set("")
        AGE.set("")
        GENDER.set("")
        TELEPHONE.set("")
        MOBILE.set("")
        OFFICE.set("")
        EMAIL.set("")
        ADDRESS.set("")
        RELATION.set("")
        
#------------------------------------------------------- EDIT -------------------------------------------------------------------------------------------------------------------------      

def edit_data(event):
    global S_No, EditContact

    cursor_item = table.focus()
    contents = (table.item(cursor_item))
    selected_item = contents['values']
    S_No = selected_item[0]

    NAME.set("")
    AGE.set("")
    GENDER.set("")
    TELEPHONE.set("")
    MOBILE.set("")
    OFFICE.set("")
    EMAIL.set("")
    ADDRESS.set("")
    RELATION.set("")

    NAME.set(selected_item[1])
    AGE.set(selected_item[2])
    GENDER.set(selected_item[3])
    TELEPHONE.set(selected_item[4])
    MOBILE.set(selected_item[5])
    OFFICE.set(selected_item[6])
    EMAIL.set(selected_item[7])
    ADDRESS.set(selected_item[8])
    RELATION.set(selected_item[9])

    EditContact = Toplevel()
    EditContact.title("Edit Contact")
    EditContact.iconbitmap('D:\\Address_Book\\icon\\contact.ico')
    EditContact.geometry("500x380")
    EditContact.config(bg = 'gainsboro')

    #=================== FRAMES ===========================================================================================================================================================

    title_frame = Frame(EditContact, bg = 'gainsboro')
    title_frame.pack(side=TOP)

    data_frame = Frame(EditContact, bg = 'gainsboro')
    data_frame.pack(side=TOP, pady=10)

    gender_btn = Frame(data_frame, bg = 'gainsboro')

    relation_btn = Frame(data_frame, bg = 'gainsboro')

    #====================================================================================================================================================================================

    Male = Radiobutton(gender_btn, text="Male", variable=GENDER, value="male",  font=('Kristen ITC', 10), fg = 'black', bg="gainsboro").pack(side=LEFT)
    Female = Radiobutton(gender_btn, text="Female", variable=GENDER, value="female",  font=('Kristen ITC', 10), fg = 'black', bg="gainsboro").pack(side=LEFT)

    Family = Radiobutton(relation_btn, text="Family", variable=RELATION, value="Family",  font=('Kristen ITC', 10), fg = 'black', bg="gainsboro").pack(side=LEFT)
    Friends = Radiobutton(relation_btn, text="Friends", variable=RELATION, value="Friends",  font=('Kristen ITC', 10), fg = 'black', bg="gainsboro").pack(side=LEFT)
    Work = Radiobutton(relation_btn, text="Work", variable=RELATION, value="Work",  font=('Kristen ITC', 10), fg = 'black', bg="gainsboro").pack(side=LEFT)
    Others = Radiobutton(relation_btn, text="Others", variable=RELATION, value="Others",  font=('Kristen ITC', 10), fg = 'black', bg="gainsboro").pack(side=LEFT)
   
    #===================LABELS===========================================================================================================================================================

    lbl_title = Label(title_frame, text="Edit Contact", font =("Harlow Solid Italic", 15), bg="gainsboro", fg = 'grey18', width = 300)
    lbl_title.pack(fill=X)

    lbl_name = Label(data_frame, text="Name:", font =("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_name.grid(row=1, sticky=W)

    lbl_age = Label(data_frame, text="Age:", font =("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_age.grid(row=2, sticky=W)

    lbl_gender = Label(data_frame, text="Gender:", font =("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_gender.grid(row=3, sticky=W)    

    lbl_phone = Label(data_frame, text="TelePhone:", font= ("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_phone.grid(row=4, sticky=W)

    lbl_phone = Label(data_frame, text="Mobile:", font= ("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_phone.grid(row=5, sticky=W)

    lbl_phone = Label(data_frame, text="Office:", font= ("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_phone.grid(row=6, sticky=W)

    lbl_email = Label(data_frame, text="Email:", font= ("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_email.grid(row=7, sticky=W)

    lbl_address = Label(data_frame, text="Address:", font =("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_address.grid(row=8, sticky=W)

    lbl_relation = Label(data_frame, text="Relation:", font =("Comic Sans MS", 10, 'bold'), bg = 'gainsboro', fg = 'black', bd=5)
    lbl_relation.grid(row=9, sticky=W)

    #==================BUTTONS===========================================================================================================================================================

    save_btn = Button(data_frame, text = "Save", width = 10, font = ('Bodoni MT', 12, 'bold'), bg = 'gainsboro', fg = 'brown1', activebackground = 'grey74', activeforeground = 'black', relief = FLAT, command = edit)
    save_btn.grid(row = 12)

    cancel_btn = Button(data_frame, text = 'Cancel', width = 10, font = ('Bodoni MT', 12, 'bold'), bg = 'gainsboro', fg = 'brown1', activebackground = 'grey74', activeforeground = 'black', relief = FLAT, command = edit_cancel)
    cancel_btn.grid(row = 12,column = 2)

    #======================================== ENTRYS ====================================================================================================================================

    name = Entry(data_frame, textvariable=NAME, font= ('Kristen ITC', 10))
    name.grid(row=1, column=1)

    age = Entry(data_frame, textvariable=AGE, font= ('Kristen ITC', 10))
    age.grid(row=2, column=1)

    gender_btn.grid(row=3, column=1)

    telephone = Entry(data_frame, textvariable=TELEPHONE, font= ('Kristen ITC', 10))
    telephone.grid(row=4, column=1)

    mobile = Entry(data_frame, textvariable=MOBILE, font= ('Kristen ITC', 10))
    mobile.grid(row=5, column=1)

    office = Entry(data_frame, textvariable=OFFICE, font= ('Kristen ITC', 10))
    office.grid(row=6, column=1)

    email = Entry(data_frame, textvariable=EMAIL,  font= ('Kristen ITC', 10))
    email.grid(row=7, column=1)

    address = Entry(data_frame, textvariable=ADDRESS, font= ('Kristen ITC', 10))
    address.grid(row=8, column=1)

    relation_btn.grid(row=9, column=1)
    
#------------------------------------------------------------ ADD ------------------------------------------------------------------------------------------------------------------------    

def add():

    global AddContact

    NAME.set("")
    AGE.set("")
    GENDER.set("")
    TELEPHONE.set("")
    MOBILE.set("")
    OFFICE.set("")
    EMAIL.set("")
    ADDRESS.set("")
    RELATION.set("")

    AddContact = Toplevel()
    AddContact.title("Add Contact")
    AddContact.iconbitmap('D:\\Address_Book\\icon\\contact.ico')
    AddContact.geometry("500x380")
    AddContact.config(bg = 'pink')

    #===================FRAMES===========================================================================================================================================================

    title_frame = Frame(AddContact, bg = 'pink')
    title_frame.pack(side=TOP)

    data_frame = Frame(AddContact, bg = 'pink')
    data_frame.pack(side=TOP, pady=10)

    gender_btn = Frame(data_frame, bg = 'pink')

    relation_btn = Frame(data_frame, bg = 'pink')

    #====================================================================================================================================================================================

    Male = Radiobutton(gender_btn, text="Male", variable=GENDER, value="male",  font=('Kristen ITC', 10), fg = 'black', bg="pink").pack(side=LEFT)
    Female = Radiobutton(gender_btn, text="Female", variable=GENDER, value="female",  font=('Kristen ITC', 10), fg = 'black', bg="pink").pack(side=LEFT)

    Family = Radiobutton(relation_btn, text="Family", variable=RELATION, value="Family",  font=('Kristen ITC', 10), fg = 'black', bg="pink").pack(side=LEFT)
    Friends = Radiobutton(relation_btn, text="Friends", variable=RELATION, value="Friends",  font=('Kristen ITC', 10), fg = 'black', bg="pink").pack(side=LEFT)
    Work = Radiobutton(relation_btn, text="Work", variable=RELATION, value="Work",  font=('Kristen ITC', 10), fg = 'black', bg="pink").pack(side=LEFT)
    Others = Radiobutton(relation_btn, text="Others", variable=RELATION, value="Others",  font=('Kristen ITC', 10), fg = 'black', bg="pink").pack(side=LEFT)
   
    #===================LABELS===========================================================================================================================================================

    lbl_title = Label(title_frame, text="Add Contact", font =("Harlow Solid Italic", 15), bg="pink", fg = 'grey18', width = 300)
    lbl_title.pack(fill=X)

    lbl_name = Label(data_frame, text="Name:", font =("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_name.grid(row=1, sticky=W)

    lbl_age = Label(data_frame, text="Age:", font =("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_age.grid(row=2, sticky=W)

    lbl_gender = Label(data_frame, text="Gender:", font =("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_gender.grid(row=3, sticky=W)    

    lbl_phone = Label(data_frame, text="TelePhone:", font= ("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_phone.grid(row=4, sticky=W)

    lbl_phone = Label(data_frame, text="Mobile:", font= ("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_phone.grid(row=5, sticky=W)

    lbl_phone = Label(data_frame, text="Office:", font= ("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_phone.grid(row=6, sticky=W)

    lbl_email = Label(data_frame, text="Email:", font= ("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_email.grid(row=7, sticky=W)

    lbl_address = Label(data_frame, text="Address:", font =("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_address.grid(row=8, sticky=W)

    lbl_relation = Label(data_frame, text="Relation:", font =("Comic Sans MS", 10, 'bold'), bg = 'pink', fg = 'black', bd=5)
    lbl_relation.grid(row=9, sticky=W)

    #======================================== ENTRYS ====================================================================================================================================

    name = Entry(data_frame, textvariable=NAME, font= ('Kristen ITC', 10))
    name.grid(row=1, column=1)

    age = Entry(data_frame, textvariable=AGE, font= ('Kristen ITC', 10))
    age.grid(row=2, column=1)

    gender_btn.grid(row=3, column=1)

    telephone = Entry(data_frame, textvariable=TELEPHONE, font= ('Kristen ITC', 10))
    telephone.grid(row=4, column=1)

    mobile = Entry(data_frame, textvariable=MOBILE, font= ('Kristen ITC', 10))
    mobile.grid(row=5, column=1)

    office = Entry(data_frame, textvariable=OFFICE, font= ('Kristen ITC', 10))
    office.grid(row=6, column=1)

    email = Entry(data_frame, textvariable=EMAIL,  font= ('Kristen ITC', 10))
    email.grid(row=7, column=1)

    address = Entry(data_frame, textvariable=ADDRESS, font= ('Kristen ITC', 10))
    address.grid(row=8, column=1)

    relation_btn.grid(row=9, column=1)

    #==================BUTTONS===================================================================================================================================================================================================

    save_btn = Button(data_frame, text = "Save", width = 10, font = ('Bodoni MT', 12, 'bold'), bg = 'pink', fg = 'deepskyblue4', activebackground = 'gainsboro', activeforeground = 'black', relief = FLAT, command = save)
    save_btn.grid(row = 12)

    cancel_btn = Button(data_frame, text = 'Cancel', width = 10, font = ('Bodoni MT', 12, 'bold'), bg = 'pink', fg = 'deepskyblue4', activebackground = 'gainsboro', activeforeground = 'black', relief = FLAT, command = add_cancel)
    cancel_btn.grid(row = 12,column = 2)

#----------------------------------------------- MAIN WINDOW --------------------------------------------------------------------------------------------------------------------------------------------------------------------

#============================================= FRAMES ===========================================================================================================================================================================

title_frame = Frame(root, width = 500, relief = SOLID)
title_frame.pack(side = TOP)

btn_frame = Frame(root, width=700,  bg = "powderblue")
btn_frame.pack(side = TOP)

lbtn_frame = Frame(btn_frame, width = 100)
lbtn_frame.pack(side = LEFT, pady = 10)

lbtn_Padding = Frame(btn_frame, width = 700, bg = "powderblue")
lbtn_Padding.pack(side = LEFT)

rbtn_frame = Frame(btn_frame, width = 100)
rbtn_frame.pack(side = RIGHT, pady = 10)

Table_Margin = Frame(root, width = 500)
Table_Margin.pack(side = TOP, expand = True)

#============================================= TITLE ====================================================================================================================================

lbl_title = Label(title_frame, text = "ADDRESS BOOK", font = ("forte", 20), fg = 'grey1', bg = "powderblue").pack(fill = X)

#================================================ BUTTONS ===============================================================================================================================

dltbtn_img = PhotoImage(file = 'D:\\Address_Book\\icon\\delete.png')
btn_dlt = Button(rbtn_frame, image = dltbtn_img, bg = "powderblue", relief = FLAT, command = delete).pack(side = RIGHT)

addbtn_img = PhotoImage(file = 'D:\\Address_Book\\icon\\add.png')
btn_add = Button(lbtn_frame, image = addbtn_img, bg = "powderblue", relief = FLAT, command = add).pack(side = LEFT)

#================================================= TABLE DATA ===========================================================================================================================

scrollbarx = Scrollbar(Table_Margin, orient = HORIZONTAL)
scrollbary = Scrollbar(Table_Margin, orient = VERTICAL)

style = ttk.Style()
style.configure("Treeview.Heading", font = 'algerian 11')

table = ttk.Treeview(Table_Margin, columns=("S_NO", "NAME", "AGE", "GENDER", "TELEPHONE", "MOBILE", "OFFICE", "EMAIL", "ADDRESS", "RELATION"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

scrollbary.config(command = table.yview)
scrollbary.pack(side = RIGHT, fill=Y)
scrollbarx.config(command = table.xview)
scrollbarx.pack(side = BOTTOM, fill=X)

table.heading('S_NO', text = "S_NO", anchor = W)
table.heading('NAME', text = "NAME", anchor = W)
table.heading('AGE', text = "AGE", anchor = W)
table.heading('GENDER', text = "GENDER", anchor = W)
table.heading('TELEPHONE', text = "TELEPHONE", anchor = W)
table.heading('MOBILE', text = "MOBILE", anchor = W)
table.heading('OFFICE', text = "OFFICE", anchor = W)
table.heading('EMAIL', text = "EMAIL", anchor = W)
table.heading('ADDRESS', text = "ADDRESS", anchor = W)
table.heading('RELATION', text = "RELATION", anchor = W)


table.column('#0', stretch = NO, minwidth = 1, width = 0)
table.column('#1', stretch = NO, minwidth = 1, width = 45)
table.column('#2', stretch = NO, minwidth = 1, width = 120)
table.column('#3', stretch = NO, minwidth = 1, width = 45)
table.column('#4', stretch = NO, minwidth = 1, width = 80)
table.column('#5', stretch = NO, minwidth = 1, width = 90)
table.column('#6', stretch = NO, minwidth = 1, width = 90)
table.column('#7', stretch = NO, minwidth = 1, width = 90)
table.column('#8', stretch = NO, minwidth = 1, width = 180)
table.column('#9', stretch = NO, minwidth = 1, width = 150)
table.column('#10', stretch = NO, minwidth = 1, width = 80)

table.bind('<Double-Button-1>', edit_data)

table.pack()

#============================================================= INITIALISATION =============================================================================================================

if __name__ == '__main__':
    Database()
    root.mainloop()
