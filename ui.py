from tkinter import *
from tkinter import messagebox
THEME_COLOR = "#375362"
class QuizInterface:
	def __init__(self,quiz_brain):
		self.r=0
		self.t=0
		self.quiz=quiz_brain
		self.window=Tk()
		self.window.title("Quizzler")
		self.window.config(padx=20,pady=20,bg=THEME_COLOR)
		self.canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0)
		self.qtext=self.canvas.create_text(150,125,text="Hello",font=("Arial",20,"italic"),fill="black",width=280)
		self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
		
		true_img = PhotoImage(file="images/true.png")
		self.true_button = Button(image=true_img, highlightthickness=0,padx=20,pady=20,command=self.check_ans_true)
		self.true_button.grid(row=2, column=0)
	
		false_img = PhotoImage(file="images/false.png")
		self.false_button = Button(image=false_img, highlightthickness=0,padx=20,pady=20,command=self.check_ans_false)
		self.false_button.grid(row=2, column=1)
		
		self.label=Label(text=f"Score : {self.r}/{self.t}", fg="white",bg=THEME_COLOR, font=("Calibri",10,"normal"),pady=20)
		self.label.grid(row=0,column=1)
		
		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		self.q_text=self.quiz.next_question()
		if self.q_text=="over":
			self.gameover()
		self.canvas.itemconfig(self.qtext,text=self.q_text)
	
	def check_ans_true(self):
		if self.quiz.ret_ans().lower()=="true":
			self.r+=1
		self.t+=1
		self.label.config(text=f"Score : {self.r}/{self.t}")
		self.get_next_question()
		
	def gameover(self):
		messagebox.showinfo(title="Game Over.",message=f"Final score : {self.r}/10")
		quit()
	
	def check_ans_false(self):
		if self.quiz.ret_ans().lower()=="false":
			self.r+=1
		self.t+=1
		self.label.config(text=f"Score : {self.r}/{self.t}")
		self.get_next_question()
