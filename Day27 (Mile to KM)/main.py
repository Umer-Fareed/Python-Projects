from tkinter import *

def button_clicked():
    print("i got clicked ")
    new_text= input.get()
    my_label.config(text=new_text)

window= Tk()
window.title("My First GUI Program")
window.minsize(width= 500 , height= 300)
#add space around your window
window.config(padx= 20, pady= 100)

#label
my_label= Label(text= "I am label", font= ("Times new roman", 24, "bold"))
#my_label.pack()
#my_label.place(x= 0, y= 0)
my_label.grid(column= 0 , row= 0)

#Button
button= Button(text= " Click me ", command=button_clicked)
#button.pack()
button.grid(column= 1, row= 1)

#2nd button
button2= Button(text= " 2nd button")
button2.grid(column= 2, row= 0)

#entry
input= Entry(width=30 )
#input.pack()
input.grid(column=3 , row= 3)
input.get()









window.mainloop()