from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry, END, Spinbox, messagebox
import random
import pyperclip
import json

PASSWORD_LENGTH = 8


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    alphabet = "".join(chr(x) for x in range(32, 127))

    rand_pass = "".join([alphabet[random.randint(0, 94)]
                        for i in range(0, PASSWORD_LENGTH)])
    password_box.delete(0, END)
    password_box.insert(END, rand_pass)
    pyperclip.copy(password_box.get())  # Copies New Password to Clipboard





# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_password():

    new_data = {
        website_box.get(): {
            "email": email_box.get(),
            "password": password_box.get()
        }
    }

    if len(website_box.get()) == 0 or website_box.get() == "Website Placeholder Text" or len(email_box.get()) == 0 or email_box.get() == "You@YourEmail.com" or len(password_box.get()) == 0 or password_box.get() == "Password Placeholder Text":
        messagebox.showerror(
            title="Error", message="Please don't leave fields blank or on default values")
        return

    is_ok = messagebox.askokcancel(title=website_box.get(
    ), message=f"These are the details entered: \nEmail: {email_box.get()} \nPassword:{password_box.get()}")

    if is_ok == True:
        try:
            with open("/Users/Cook/Documents/VS Code/Day 23 - Password Manager/Password Generator/data.json", mode="r") as f:
                # Reading data
                data = json.load(f)

        except FileNotFoundError:

            with open("/Users/Cook/Documents/VS Code/Day 23 - Password Manager/Password Generator/data.json", mode="w") as f:

                # loading data
                json.dump(new_data, f, indent=4)
        else:
            # Updating data
            data.update(new_data)

            with open("/Users/Cook/Documents/VS Code/Day 23 - Password Manager/Password Generator/data.json", mode="w") as f:
                # Writing updated data
                json.dump(data, f, indent=4)

        finally:
            website_box.delete(0, END)
            password_box.delete(0, END)



def search():
    try:
        with open("/Users/Cook/Documents/VS Code/Day 23 - Password Manager/Password Generator/data.json", mode="r") as f:
            #Reading data
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File Not Found")
    else:
        if website_box.get() in data:
            email = data[website_box.get()]["email"]
            password = data[website_box.get()]["password"]
            messagebox.showinfo(title=website_box.get(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_box.get()} exist.")

# ---------------------------- UI SETUP ------------------------------- #
# Makes Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize()

# Makes Background, Imports Logo, Places Logo on Screen w/ Grid
canvas = Canvas(width=200, height=189, highlightthickness=0)
logo = PhotoImage(
    file="/Users/Cook/Documents/VS Code/Day 23 - Password Manager/Password Generator/logo.png")
canvas.create_image(100, 95, image=logo)
canvas.grid(row=2, column=2)  # need to have this to place images/widgets

# Makes the On Screen Buttons, Widgets, Entries, Etc.
execute = Button(text="Generate Password", command=generate)
execute.grid(row=6, column=3)

add_button = Button(text="Add", command=write_password)
add_button.grid(row=7, column=2, columnspan=3, sticky="nsew")

search_button = Button(text="Search", command=search)
search_button.grid(row=3, column=3, columnspan=2, sticky="nsew")

website_label = Label(text="Website: ")
website_label.grid(row=3, column=1)

website_box = Entry()
website_box.insert(END, string="Website Placeholder Text")
website_box.grid(row=3, column=2, sticky="nsew")

email_label = Label(text="Email/Username: ")
email_label.grid(row=4, column=1)

email_box = Entry()
email_box.insert(END, string="You@YourEmail.com")
email_box.grid(row=4, column=2, columnspan=3, sticky="nsew")

password_label = Label(text="Password: ")
password_label.grid(row=6, column=1)

password_box = Entry()
password_box.insert(END, string="Password Placeholder Text")
password_box.grid(row=6, column=2, sticky="w")


def spinbox_used():
    # gets the current value in spinbox.
    global PASSWORD_LENGTH
    PASSWORD_LENGTH = int(spinbox.get())


spinbox = Spinbox(from_=8, to=30, width=5, command=spinbox_used)
spinbox.grid(row=5, column=2, columnspan=2, sticky="nsew")

spinbox_label = Label(text="Password Length")
spinbox_label.grid(row=5, column=1)


window.mainloop()
