from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry, END, Spinbox, messagebox
import random
import pyperclip

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
    if len(website_box.get()) == 0 or website_box.get() == "Website Placeholder Text" or len(email_box.get()) == 0 or email_box.get() == "You@YourEmail.com" or len(password_box.get()) == 0 or password_box.get() == "Password Placeholder Text":
        messagebox.showerror(title="Error", message="Please don't leave fields blank or on default values")
        return

    is_ok = messagebox.askokcancel(title=website_box.get(
    ), message=f"These are the details entered: \nEmail: {email_box.get()} \nPassword:{password_box.get()}")

    

    if is_ok == True:
        with open("/Users/Cook/Documents/VS Code/Day 23 - Password Manager/passwords.txt", mode="a") as f:
            f.writelines(" | ".join(
                [website_box.get(), email_box.get(), password_box.get()]))
            f.writelines("\n")
            website_box.delete(0,END)
            password_box.delete(0,END)
            f.close()


# ---------------------------- UI SETUP ------------------------------- #
# Makes Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize()

# Makes Background, Imports Logo, Places Logo on Screen w/ Grid
canvas = Canvas(width=200, height=189, highlightthickness=0)
logo = PhotoImage(
    file="/Users/Cook/Documents/VS Code/Day 23 - Password Manager/logo.png")
canvas.create_image(100, 95, image=logo)
canvas.grid(row=2, column=2)  # need to have this to place images/widgets

# Makes the On Screen Buttons, Widgets, Entries, Etc.
execute = Button(text="Generate Password", command=generate)
execute.grid(row=6, column=3)

add_button = Button(text="Add", command=write_password)
add_button.grid(row=7, column=2, columnspan=3, sticky="nsew")

website_label = Label(text="Website: ")
website_label.grid(row=3, column=1)

website_box = Entry()
website_box.insert(END, string="Website Placeholder Text")
website_box.grid(row=3, column=2, columnspan=3, sticky="nsew")

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
    print(spinbox.get())


spinbox = Spinbox(from_=8, to=30, width=5, command=spinbox_used)
spinbox.grid(row=5, column=2, columnspan=2, sticky="nsew")

spinbox_label = Label(text="Password Length")
spinbox_label.grid(row=5, column=1)


window.mainloop()
