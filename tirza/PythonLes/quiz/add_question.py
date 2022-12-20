#function to add questions to our quiz
import json


def import_questions():
    '''Import questions from 'questions.json'.'''
    with open('questions.json', 'r', encoding='UTF-8') as file:
        questions = json.load(file)
    return questions


def add_question():
    questions = import_questions()
    question = input("Enter Question: \n")
    a = input("Enter Answer A: \n")
    b = input("Enter Answer B: \n")
    c = input("Enter Answer C: \n")
    d = input("Enter Answer D: \n")
    answer = input("Correct answer (A,B,C or D)")
    entry = {"question" : question,"a" : a,"b" : b,"c" : c,"d" : d,"answer" : answer,}
    questions.append(entry)
    with open('questions.json', 'w', encoding='UTF-8') as file:
        json.dump(questions, file, indent = 4)


add_question()




