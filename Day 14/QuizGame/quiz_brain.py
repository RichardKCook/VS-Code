class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.results = 0

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def check_answer(self, guess, answer):
        if guess == answer:
            print("You got it right!")
            self.results += 1
        else:
            print(f"Sorry that's not right, the correct answer was {answer.title()}")
        print(f"Your current score is {self.results}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(
            f"Q.{self.question_number} {current_question.question} (True/False): ").lower()
        self.check_answer(guess, current_question.answer)
        print("\n")
