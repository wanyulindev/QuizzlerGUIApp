from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while we test tkinter ui.py,
# window.mainloop() mainly working like a forever running loop to listen what we do inside
# the interface. So it would be tricky if we have another while loop just besides it,
# it would cause interruptions (see down we have another while loop).
# So let's hide it for now:

# while quiz.still_has_questions():
#     quiz.next_question()

print(f"You've completed the quiz\n"
      f"Your final score was: {quiz.score}/{quiz.question_number}")


