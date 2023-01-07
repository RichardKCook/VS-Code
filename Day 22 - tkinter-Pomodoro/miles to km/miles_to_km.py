from tkinter import *

window = Tk()
window.minsize()
window.title("Miles to Km Converter")
window.config(padx=20,pady=10)


def conv():
    
    km = "{:.2f}".format(int(entry.get())*1.609344)
    result.config(text=km) #must be a string, but format function returns string


#make static unit for miles
miles_label = Label(text="Miles")
miles_label.grid(row=1,column=3)

#make static filler text
iet_label = Label(text="is equal to",justify="right")
iet_label.grid(row=2,column=1)

#make static unit for Km
km_label = Label(text="Km")
km_label.grid(row=2,column=3)

#make dynamic field to display result
result = Label(text=0)
result.grid(row=2,column=2)

#make input box with filled 0
entry = Entry(width=5)
entry.insert(END,string="0")
entry.grid(row=1,column=2)

#make command button
button = Button(text="Calculate",command=conv)
button.grid(row=3,column=2)




window.mainloop()