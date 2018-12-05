Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from Question import Question
question prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n" ,
    "What Color are Bananas?\n(a) Teal\(b) Magenta\n(c) Yellow\n\n" ,
    "What Color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

class Question:
    def__init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer
    from Question import Question

questions = [
    Question(question_prompts[0], "a")
    Question(question_prompts[1], "c")
    Question(question_prompts[2], "b")

def run_test(questions)
    score = 0
    for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
        score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

def run_test(questions):
    score = 0
    for question in questions:
    
    
