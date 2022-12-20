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


def check_answer(question, correct_answer):
    '''Checks the given answer for the right answer to the question.'''
    answer_input = check_input()
    if question['answer'] == answer_input:
        print('\nThat is correct!\n')
        correct_answer += 1
        print(f'Your score: {correct_answer}')
        return correct_answer
    else:
        print(f'\nNice try! The correct answer is {question["answer"].upper()}\n')
        print(f'Your score: {correct_answer}')


def loop_questions(questions, player_name, correct_answer):
    '''Loops through the questions and keeps track of the answer.'''
    for question in questions:
        print('\n')
        for key, value in question.items():
            if key != 'answer':
                print(f'{key.title()}: {value}')
            else:
                continue
        correct_answer = check_answer(question, correct_answer)


def show_scores():
    '''Import high scores from file high_scores.json'.'''
    with open('high_scores.json', 'r', encoding='UTF-8') as file:
        high_scores = json.load(file)
        for key, value in high_scores.items():
            print(f'Player {key.title()} has {value} points.')


def update_scores(player_name, correct_answer):
    with open('high_scores.json', 'r') as file:
        high_scores = json.load(file)
    if player_name in high_scores:
        if correct_answer >= high_scores[player_name]:
            high_scores[player_name] = correct_answer
    with open('high_scores.json', 'w', encoding='UTF-8') as file:
        json.dump(high_scores, file, indent = 4)


def main():
    while True:
        player_name = input('What is your name?\n')
        questions = import_questions()
        questions = random.sample(questions, k=5)
        correct_answer = 0
        choice = input('''What whould you like to do?\n1. Take the quiz!\
            \n2. Add a question\n3. Show high scores\n4. Quit\n''')
        if choice == '1':
            correct_answer = loop_questions(questions, player_name, correct_answer)
            update_scores(player_name, correct_answer)
        elif choice == '2':
            add_question(questions)
        elif choice == '3':
            show_scores()
        elif choice == '4':
            break
        else:
            print("Invalid input, please choose '1', '2', '3' or '4'.")


if __name__ == '__main__':
    main()
