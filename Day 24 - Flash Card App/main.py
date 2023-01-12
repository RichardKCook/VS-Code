from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry, END, Spinbox, messagebox
import data_handler

BACKGROUND_COLOR = "#B1DDC6"
KNOWN_WORD = ""


# Get Data --------------------------------------------------------------------
def get():
    global data
    data = data_handler.Data_Handler()

    pair = data.get_words()
    global french_word
    french_word = pair[0]
    global english_word
    english_word = pair[1]


def wrong():

    get()
    card.itemconfig(card_side, image=card_front)
    card.itemconfig(title_display, text="French")
    card.itemconfig(word_display, text=french_word)
    window.after(3000, func=flip)

def right():
    
    get()
    card.itemconfig(card_side, image=card_front)
    card.itemconfig(title_display, text="French")
    card.itemconfig(word_display, text=french_word)
    KNOWN_WORDS = french_word
    data.words_to_learn(KNOWN_WORD)
    window.after(3000, func=flip)

def flip():
    card.itemconfig(card_side, image=card_back)
    card.itemconfig(title_display, text="English")
    card.itemconfig(word_display, text=english_word)


# Interface Setup----------------------------------------------------------------
get()
window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)
window.minsize()

# If you don't put 'file=' then it won't work
checkmark = PhotoImage(
    file="/Users/Cook/Documents/VS Code/Day 24 - Flash Card App/images/right.png")

ex = PhotoImage(
    file="/Users/Cook/Documents/VS Code/Day 24 - Flash Card App/images/wrong.png")

card_front = PhotoImage(
    file="/Users/Cook/Documents/VS Code/Day 24 - Flash Card App/images/card_front.png")

card_back = PhotoImage(
    file="/Users/Cook/Documents/VS Code/Day 24 - Flash Card App/images/card_back.png")


checkmark_button = Button(
    image=checkmark, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, background=BACKGROUND_COLOR,command=right)

checkmark_button.grid(row=2, column=1)

ex_button = Button(image=ex, highlightthickness=0,
                   highlightcolor=BACKGROUND_COLOR, background=BACKGROUND_COLOR, command=wrong)

ex_button.grid(row=2, column=2)

card = Canvas(width=800, height=526,
              highlightbackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR, highlightthickness=0)

card_side = card.create_image(400, 263, image=card_front)

global title_display
title_display = card.create_text(
    400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
global word_display
word_display = card.create_text(
    400, 263, text=french_word, font=("Arial", 60, "bold"), fill="black")
card.grid(row=1, column=1, columnspan=2, sticky="nsew")

window.after(3000, func=flip)



card.config()

window.mainloop()
