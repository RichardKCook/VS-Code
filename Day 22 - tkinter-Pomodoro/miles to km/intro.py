from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

my_label = Label(text="This is my label",font=("Arial", 24, "bold"))
my_label.grid(row=1,column=1)

my_label["text"] = "temp text"


def button_clicked():
    if my_label["text"] == "final text":
        my_label.config(text="temp text")
    else:    
        my_label.config(text="final text")

button = Button(text="temp to final", command=button_clicked)
button.grid(row=2,column=2)



def name():
    name = input.get()
    my_label.config(text=name)
    #my_label.grid(column=2,row=4)



input = Entry()
input.insert(END, string="Something to begin with")
input.grid(row=3, column=4)

button2 = Button(text="Box to Screen", command=name)
button2.grid(row=1, column=3)





window.mainloop()


