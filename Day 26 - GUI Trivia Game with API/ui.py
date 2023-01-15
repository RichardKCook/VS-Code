from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class Quiz_Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize()
        self.canvas = Canvas(width=300, height=250,
                             highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="some text", fill=THEME_COLOR, font=("Ariel, 18"),width=280)

        self.canvas.grid(column=1, row=2, columnspan=2, sticky="nsew", pady=50)

        true_image = PhotoImage(
            file="/Users/Cook/Documents/VS Code/Day 26 - GUI Trivia Game/images/true.png")

        false_image = PhotoImage(
            file="/Users/Cook/Documents/VS Code/Day 26 - GUI Trivia Game/images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0,command=self.check_the_answer_true)
        self.true_button.grid(column=1, row=3)

        self.false_button = Button(
            image=false_image, highlightthickness=0,command=self.check_the_answer_false)
        self.false_button.grid(column=2, row=3)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions() is False:

            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\n\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        q_text = self.quiz.next_question()
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.itemconfig(self.question_text, text=q_text)
    
    def check_the_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        
        

    def check_the_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        
        
    
    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)