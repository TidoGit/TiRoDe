'''Loop through the 'questions.json' file to ask questions and keep track of the
answers.'''


import json


def import_questions():
    '''Import questions from 'questions.json'.'''
    with open('questions.json', 'r', encoding='UTF-8') as file:
        questions = json.load(file)
    return questions


def loop_questions(questions):
    '''Loops through the questions and keeps track of the answer.'''
    for question in questions:
        for key, value in questions[question].items():
            if key != 'answer':
                print(f'{key.upper()} : {value}')
            else:
                continue


if __name__ == '__main__':
    questions = import_questions()
    loop_questions(questions)