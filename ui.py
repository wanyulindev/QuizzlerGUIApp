from tkinter import *
from data import question_data
from quiz_brain import QuizBrain
import random

# THEME_COLOR = "#375362"
YELLOW = "#f7f5dd"
EGGSHELL = "#FCE6C9"
LAVENDERBLUSH2 = "#EEE0E5"
LIGHTBLUE3 = "#9AC0CD"
FONT_NAME = "Calibri"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        # start writing my codes here:
        self.window.config(padx=20, pady=20, bg=EGGSHELL)

        self.score = Label(text=f"SCORE: 0", font=(FONT_NAME, 14),
                           fg=LIGHTBLUE3, bg=EGGSHELL)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg=LIGHTBLUE3, highlightthickness=0)
        self.canvas.create_image(150, 125)
        self.random = random.choice(question_data)
        self.text = self.canvas.create_text(150, 125, text=self.random["question"],
                                            font=(FONT_NAME, 20, "italic"), width=250,
                                            fill=LAVENDERBLUSH2)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=18)

        self.true_image = PhotoImage(file="images/true.png").subsample(3, 3)
        self.true = Button(image=self.true_image, highlightbackground=EGGSHELL)
        self.true.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png").subsample(3, 3)
        self.false = Button(image=self.false_image, highlightbackground=EGGSHELL)
        self.false.grid(column=1, row=2)

        self.window.mainloop()
