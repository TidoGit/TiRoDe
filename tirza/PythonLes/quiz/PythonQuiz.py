
questions = [
  				{
        "question": "question1",
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "answer": "a"
    },
    			{
        "question": "question1",
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "answer": "b"
    }
 ]



"""Check if input is equal to the answer."""
def check_input():
	options = ['a', 'b', 'c', 'd']
	while True:
		answer_input = input('What is the correct answer? ').lower()
		if answer_input in options:
			return answer_input
		else:
			print('FOUTJE')
			continue


def check_answer():
	correct_answer = 0
	for question in questions:
		answer_input = check_input()
		if question['answer'] == answer_input:
			print('That is correct!')
			correct_answer += 1
			print(correct_answer)
		else:
			print(f'Nice try! The correct answer is {question["answer"]}')


check_answer()
