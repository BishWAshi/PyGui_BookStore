#-------------------------------------------------------------------------------
# Name:        module1 - Front End GUI
# Purpose:
#
# Author:      Admin
#
# Created:     29-01-2018
# Copyright:   (c) Admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import backend

def selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:                # This will remove error if there is nothing in the list
        pass





def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get())
    list1.delete(0,END)
    list1.insert(END,(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get())


window=Tk()
window.wm_title("BookStore")           # Window Title

title_lbl=Label(window,text="Title")
title_lbl.grid(row=0,column=0)
# Entry field
title_txt=StringVar()
e1=Entry(window,textvariable=title_txt)
e1.grid(row=0,column=1)

author_lbl=Label(window,text="Author")
author_lbl.grid(row=0,column=2)

author_txt=StringVar()
e2=Entry(window,textvariable=author_txt)
e2.grid(row=0,column=3)

year_lbl=Label(window,text="Year")
year_lbl.grid(row=1,column=0)


year_txt=StringVar()
e3=Entry(window,textvariable=year_txt)
e3.grid(row=1,column=1)

isbn_lbl=Label(window,text="ISBN")
isbn_lbl.grid(row=1,column=2)

isbn_txt=StringVar()
e4=Entry(window,textvariable=isbn_txt)
e4.grid(row=1,column=3)


list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

scrollbar1=Scrollbar(window)
scrollbar1.grid(row=2,column=2, rowspan=6)
list1.configure(yscrollcommand=scrollbar1.set)    #vertical scroll bar Y
scrollbar1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",selected_row)      # Get selected row from listbox1

b1=Button(window,text="View All", width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()

def main():
    pass

if __name__ == '__main__':
    main()
