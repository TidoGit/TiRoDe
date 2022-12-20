'''
This is a quiz to check your Python knowledge.
This quiz imports the questions from the file 'questions.json.
It loops through the questions and checks the answers.
'''

 

import json
import random
 


def import_questions():
    '''Import questions from 'questions.json'.'''
    with open('questions.json', 'r', encoding='UTF-8') as file:
        questions = json.load(file)
    return questions

 


def add_question(questions):
    '''Add a question to questions.json.'''
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

 


def check_input():
    '''Checks if input is in list 'options'.'''
    options = ['a', 'b', 'c', 'd']
    while True:
        answer_input = input('What is the correct answer? ').lower()
        if answer_input in options:
            return answer_input
        else:
            print("Invalid input, please choose 'A', 'B', 'C', or 'D'.")
            continue

 


def check_answer(question):
    '''Checks the given answer for the right answer to the question.'''
    correct_answer = 0
    answer_input = check_input()
    if question['answer'] == answer_input:
        print('\nThat is correct!\n')
        correct_answer += 1
        print(f'Your score: {correct_answer}')
        return correct_answer
    else:
        print(f'\nNice try! The correct answer is {question["answer"]}\n')

 


def loop_questions(questions):
    '''Loops through the questions and keeps track of the answer.'''
    for question in questions:
        print('\n')
        for key, value in question.items():
            if key != 'answer':
                print(f'{key.title()}: {value}')
            else:
                continue
        check_answer(question)

 


def main():
    while True:
        questions = import_questions()
        questions = random.sample(questions, k=5)
        choice = input('''What whould you like to do?\n1. Take the quiz!\
            \n2. Add a question\n3. Quit\n''')
        if choice == '1':
            loop_questions(questions)
        elif choice == '2':
            add_question(questions)
        elif choice == '3':
            break
        else:
            print("Invalid input, please choose '1', '2' or '3'.")

 


if __name__ == '__main__':
    main()