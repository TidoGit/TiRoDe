#function to add questions to our quiz

questions = []

def add_question():
    question = input("Enter Question: \n")
    a = input("Enter Answer A: \n")
    b = input("Enter Answer B: \n")
    c = input("Enter Answer C: \n")
    d = input("Enter Answer D: \n")
    answer = input("Correct answer (A,B,C or D)")
    entry = {"question" : question,"a" : a,"b" : b,"c" : c,"d" : d,"answer" : answer,}
    questions.append(entry)

add_question()




