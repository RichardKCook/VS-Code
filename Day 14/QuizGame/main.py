from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

all_questions = []
for question in range(len(question_data)):

    current_question = question_data[question]

    all_questions.append(
        Question(current_question['question'], current_question['correct_answer'].lower()))


quizbrain = QuizBrain(all_questions)


print("Welcome to the Quiz Game")


while quizbrain.still_has_questions() == True:
    quizbrain.next_question()
    quizbrain.still_has_questions()


print(
    f"You finished the quiz! You got {quizbrain.results} correct! " 
    f"That's {quizbrain.results/len(all_questions)*100}%")
