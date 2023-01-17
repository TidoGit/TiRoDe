'''Python Quiz
Test your python knowledge, add your own questions and keep highscores.'''


import json
from random import sample

class Quiz:
    '''Main Program'''
    def __init__(self):
        self.questions = self.import_data('questions')
        self.scores = self.import_data('high_scores')

    def import_data(self, file_type):
        '''Import data from .json file.'''
        with open(f'{file_type}.json', 'r', encoding='UTF-8') as data:
            data_dict = json.load(data)
        return data_dict

    def export_data(self, file_type, data_dict):
        '''Export data to .json file.'''
        with open(f'{file_type}.json', 'w', encoding='UTF-8') as data:
            json.dump(data_dict, data, indent = 4)

    def display_question(self, question):
        '''Displays a single question'''
        print('\n')
        for key, value in question.items():
            if key != 'answer':
                print(f'{key.title()}: {value}')

    def check_answer(self, question):
        '''Check the given answer and returns true if correct, false otherwise.'''
        options = ['a', 'b', 'c', 'd']
        answer_input = input('Answer:\n>>> ')
        while answer_input not in options:
            print("Invalid input, please choose 'A', 'B', 'C', or 'D'.")
            answer_input = input('Answer:\n>>> ')
        correct_answer = question['answer']
        if correct_answer == answer_input.lower():
            print('\nThat is correct!')
            return True
        else:
            print(f'\nToo bad! The correct answer was {correct_answer.title()}.')
            return False

    def play(self):
        '''Loop through the questions, refer to function 'check_answer' to supply
        an answer.'''
        score = 0
        selected_questions = sample(self.questions, 5)
        for question in selected_questions:
            self.display_question(question)
            score += self.check_answer(question)
        print(f'''\n***************************\nGreat job! Your score is {score}.\
            \n***************************''')
        return score

    def add_question(self):
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
        self.questions.append(dictionary)
        self.export_data('questions', self.questions)

    def display_high_scores(self):
        '''Read and print all time high scores from file 'high_scores.json'.'''
        sorted_scores = sorted(self.scores.items(), key=lambda x:x[1], reverse=True)
        converted_scores = dict(sorted_scores)
        print('Score:   Player:')
        print('-----------------')
        for key, value in converted_scores.items():
            print(f'   {value}    {key.title()}')

    def update_high_scores(self, player_name, score):
        '''Import/export file 'high_scores.json' and add or mutate score.'''
        if player_name in self.scores:
            self.scores[player_name] += score
            self.export_data('high_scores', self.scores)
        else:
            self.scores[player_name] = score
        self.export_data('high_scores', self.scores)

    def main_menu(self):
        '''Main menu'''
        while True:
            choice = input('''\nWhat would you like to do?
            1. Play quiz
            2. Add question
            3. View high scores
            4. Quit
            \n>>> ''')
            if choice == '1':
                player_name = input('Enter your name:\n>>> ')
                score = self.play()
                self.update_high_scores(player_name, score)
            elif choice == '2':
                self.add_question()
            elif choice == '3':
                self.display_high_scores()
            elif choice == '4':
                print('Thanks for playing!')
                break
            else:
                print("Invalid input, please enter '1', '2', '3' or '4'.")

if __name__ == '__main__':
    quiz = Quiz()
    quiz.main_menu()
