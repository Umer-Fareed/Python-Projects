from tkinter import *

from ipywidgets import widget_serialization

window= Tk()

r= Label(bg= "red", width= 20, height= 5)
r.grid(row= 0, column= 0)

g= Label(bg= "green", width= 20, height= 5)
g.grid(row= 1, column= 1)

b= Label(bg= "blue", width= 20, height= 20)
b.grid(row= 2, column= 0, columnspan= 2)

window.mainloop()


def save():

    website= website_entry.get()
    email= email_entry.get()
    password= password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}")
