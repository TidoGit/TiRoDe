'''
A quiz to test your Python knowledge!
Questions and high scores are saved in separate files, the script enables you to
add a question an view the high scores.
'''

import json
import random

def import_data(file_type):
    '''Import data from .json file.'''
    with open(f'{file_type}.json', 'r', encoding='UTF-8') as data:
        data_dict = json.load(data)
    return data_dict


def export_data(file_type, data_dict):
    '''Export data to .json file.'''
    with open(f'{file_type}.json', 'w', encoding='UTF-8') as data:
        json.dump(data_dict, data, indent = 4)


def loop_questions(questions):
    '''Loop through the questions, refer to function 'check_answer' to supply
    an answer.'''
    score = 0
    for question in questions:
        print('\n')
        for key, value in question.items():
            if key != 'answer':
                print(f'{key.title()}: {value}')
            else:
                continue
        score = check_answer(question, score)
    print(f'''\n***************************\nGreat job! Your score is {score}.\
        \n***************************''')
    return score


def check_answer(question, score):
    '''Check the given answer.'''
    options = ['a', 'b', 'c', 'd']
    answer_input = input('Answer:\n>>> ')
    while answer_input not in options:
        print("Invalid input, please choose 'A', 'B', 'C', or 'D'.")
        answer_input = input('Answer:\n>>> ')
    correct_answer = question['answer']
    if correct_answer == answer_input:
        print('\nThat is correct!')
        score += 1
    else:
        print(f'\nToo bad! The correct answer was {correct_answer.title()}.')
    return score



def add_question(questions):
    '''Option to add a question to file 'questions.json'.'''
    question = input('Insert question:\n>>> ')
    option_a = input('Insert option A:\n>>> ')
    option_b = input('Insert option B:\n>>> ')
    option_c = input('Insert option C:\n>>> ')
    option_d = input('Insert option D:\n>>> ')
    answer = input('Insert correct answer:\n>>> ')
    dictionary = {
        'question' : question,
        'a' : option_a,
        'b' : option_b,
        'c' : option_c,
        'd' : option_d,
        'answer' : answer.lower(),
    }
    questions.append(dictionary)
    file_type = 'questions'
    export_data(file_type, questions)


def high_scores():
    '''Read and print all time high scores from file 'high_scores.json'.'''
    file_type = 'high_scores'
    scores = import_data(file_type)
    sorted_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    converted_scores = dict(sorted_scores)
    print('Score: | Player:')
    print('-------|--------')
    for key, value in converted_scores.items():
        print(f'   {value}   | {key.title()}')


def mutate_high_scores(player_name, score):
    '''Import/export file 'high_scores.json' and add or mutate score.'''
    file_type = 'high_scores'
    scores = import_data(file_type)
    if player_name in scores:
        if score > scores[player_name]:
            scores[player_name] = score
    else:
        scores[player_name] = score
    export_data(file_type, scores)


def main():
    '''Main menu'''
    while True:
        choice = input('''\nWhat would you like to do:\n1. Take the quiz!\
            \n2. View high scores\n3. Add a question\n4. Quit\n>>> ''')
        if choice == '1':
            file_type = 'questions'
            questions = import_data(file_type)
            questions = random.sample(questions, k = 9)
            player_name = input('Enter your name to keep the score:\n>>> ')
            score = loop_questions(questions)
            mutate_high_scores(player_name, score)
        elif choice == '2':
            high_scores()
        elif choice == '3':
            add_question(questions)
        elif choice == '4':
            break
        else:
            print('''Invalid input, please choose '1', '2', '3' or '4'.''')


if __name__ == '__main__':
    main()
