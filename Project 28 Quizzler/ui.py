from tkinter import*
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)
        self.canvas=Canvas(width=300,height=250)
        self.question_text=self.canvas.create_text(150,125,text="Some Question Text", fill=THEME_COLOR,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        
        self.right_img=PhotoImage(file=r"quizzler-app-start\images\true.png")
        self.right=Button(image=self.right_img,highlightthickness=0,command=self.true_pressed)
        self.right.grid(column=0,row=2,)
        self.wrong_img=PhotoImage(file=r"quizzler-app-start\images\false.png")
        self.wrong=Button(image=self.wrong_img,highlightthickness=0,command=self.false_pressed)
        self.wrong.grid(column=1,row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)