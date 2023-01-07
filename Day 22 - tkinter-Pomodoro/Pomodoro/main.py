from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer) # Ignore type mismatch
    background.itemconfig(timer_text, text= "00:00")
    title.config(text="Timer",fg=GREEN)
    checkmark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 == 1:
        title.config(text="Work",fg=GREEN)
        countdown(int(WORK_MIN * 60))
    elif REPS == 8:
        title.config(text="Break",fg=RED)
        countdown(int(LONG_BREAK_MIN * 60))
    elif REPS % 2 == 0:
        title.config(text="Break",fg=PINK)
        countdown(int(SHORT_BREAK_MIN * 60))


def stop_timer():
    pass # Build a Pause Function, Double Click to Reset


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    if count > -1:
        global timer
        timer = window.after(1000, countdown, count-1)
        min = count//60
        sec = count % 60

        text_time = f"{min}:{sec:02}"
        background.itemconfig(timer_text, text=text_time)
    else:
        if REPS % 2 == 1:
            global CHECKS
            CHECKS += 1
            checkmark.config(text=(CHECKS)*f"✓")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Makes Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Makes Backgound w/ Timer
background = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="/Users/Cook/Documents/VS Code/Day 22 - tkinter-Pomodoro/Pomodoro/tomato.png")
background.create_image(100, 112, image=tomato_img)
timer_text = background.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
background.grid(row=2, column=2)


# Makes Start and Reset Buttons
start = Button(text="Start", command=start_timer,
               background=YELLOW, highlightbackground=YELLOW)
start.grid(row=3, column=1)

reset = Button(text=f"Reset", command=reset_timer,
              background=YELLOW, highlightbackground=YELLOW)
reset.grid(row=3, column=3)

# Makes Labels
checkmark = Label(background=YELLOW, fg=GREEN,
                  font=(FONT_NAME, 34, "bold"))
checkmark.grid(row=4, column=2)

title = Label(text="Timer", font=(FONT_NAME, 34, "bold"),
              background=YELLOW, fg=f"{GREEN}")
title.grid(row=1, column=2)


window.mainloop()
