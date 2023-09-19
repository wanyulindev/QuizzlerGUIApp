from tkinter import *
from data import question_data
from quiz_brain import QuizBrain
import random
import html

# THEME_COLOR = "#375362"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
PINK = "#e2979c"
EGGSHELL = "#FCE6C9"
LAVENDERBLUSH2 = "#EEE0E5"
LIGHTBLUE3 = "#9AC0CD"
FONT_NAME = "Calibri"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Check out OOP (1)
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        # start writing my codes here:
        self.window.config(padx=20, pady=20, bg=EGGSHELL)

        self.current_score = Label(text=f"SCORE: 0", font=(FONT_NAME, 14),
                           fg=LIGHTBLUE3, bg=EGGSHELL)
        self.current_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg=LIGHTBLUE3, highlightthickness=0)
        self.canvas.create_image(150, 125)
        self.random = random.choice(question_data)
        self.text = self.canvas.create_text(150, 125,
                                            text=html.unescape(self.random["question"]),
                                            font=(FONT_NAME, 20, "italic"), width=250,
                                            fill=LAVENDERBLUSH2)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=18)

        self.true_image = PhotoImage(file="images/true.png").subsample(3, 3)
        self.true = Button(image=self.true_image,
                           highlightbackground=EGGSHELL,
                           command=self.if_true)
        self.true.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png").subsample(3, 3)
        self.false = Button(image=self.false_image,
                            highlightbackground=EGGSHELL,
                            command=self.if_false)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # Check out OOP (2)
        self.bg_color(LIGHTBLUE3)
        self.canvas.itemconfig(self.text,
                               font=(FONT_NAME, 20, "italic"),
                               fill=LAVENDERBLUSH2)
        self.current_score.config(text=f"SCORE: {self.quiz.score}/{self.quiz.question_number}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)

    def if_true(self):
        # answer = self.quiz.check_answer("True")
        # self.canvas.itemconfig(self.text, text=answer, font=(FONT_NAME, 28, "bold"))
        # same function as if_false(), just different writing
        self.give_feedback("True")

    def if_false(self):
        # self.canvas.itemconfig(self.text,
        #                        text=self.quiz.check_answer("False"),
        #                        font=(FONT_NAME, 28, "bold"))
        self.give_feedback("False")

    def give_feedback(self, answer):
        self.canvas.itemconfig(self.text,
                               text=self.quiz.check_answer(answer),
                               font=(FONT_NAME, 28, "bold"),
                               fill=EGGSHELL)

        # print(self.quiz.check_answer(answer))

        if answer.lower() == self.quiz.current_question.answer.lower():
            self.bg_color(GREEN)
        else:
            self.bg_color(PINK)
        # Since we always have to act before self.window.mainloop():
        self.window.after(3000, self.get_next_question)


    def bg_color(self, color):
        self.canvas.config(bg=color)



        # new commit for 9/18
        # for more commit
        # for more commit





