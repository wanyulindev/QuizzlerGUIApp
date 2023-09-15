import html
# from ui import QuizInterface

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        # self.ui = ui

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Using html module unescape function: (html entities)
        q_text = html.unescape(self.current_question.text)

        # As down below, the code serves as input:
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

        # We no longer want an input but an output that could serve and hold in the ui.py:
        # Using return:
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            # self.ui.window.after(1000, self.ui.bg_color_green)

        else:
            print("That's wrong.")
            # self.ui.window.after(1000, self.ui.bg_color_red)

        # print(f"The correct answer was: {correct_answer}.\n"
        #       f"Your current score is: {self.score}/{self.question_number}.\n")
        return (f"The correct answer was: {correct_answer}.\n"
                f"Your current score is: {self.score}/{self.question_number}.\n")
