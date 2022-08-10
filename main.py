from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface
param={
	"amount":10,
	"type":"boolean"
}
d=requests.get(url="https://opentdb.com/api.php",params=param)
question_data=d.json().get('results')
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui=QuizInterface(quiz)

