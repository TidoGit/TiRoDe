def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
    
def numbers():
    numbers = input('Choose your numbers, separated by a space: ')
    numbers = numbers.split(' ')
    numbers[0] = float(numbers[0])
    numbers[1] = float(numbers[1])
    return numbers[0], numbers[1]

while True:
    option = input('''Would you like to:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit program\n''')
    # Test for 'add' option.
    if option == '1':
        num1, num2 = numbers()
        print('%f + %f = %f' % (num1, num2, add(num1, num2)))
    # Test for 'subtract' option.
    elif option == '2':
        num1, num2 = numbers()
        print('%f - %f = %f' % (num1, num2, subtract(num1, num2)))
    # Test for 'multiply' option.
    elif option == '3':
        num1, num2 = numbers()
        print('%f * %f = %f' % (num1, num2, multiply(num1, num2)))
    # Test for 'divide' option.
    elif option == '4':
        num1, num2 = numbers()
        print('%f / %f = %f' % (num1, num2, divide(num1, num2)))
    # Test for option to stop the loop.
    elif option == '5':
        break
    # Fallback for when no supported option is selected.
    else:
        print("Invalid input, please choose a valid option (1 to 5).")