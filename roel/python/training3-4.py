def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def numbers():
    num1 = input('Choose the first number: ')
    num2 = input('Choose the second number: ')
    num1 = float(num1)
    num2 = float(num2)
    return num1, num2

option = input('Would you like to:\n1. Add\n2. Subtract\n')
# Test for 'add' option.
if option == '1':
    num1, num2 = numbers()
    print('%f + %f = %f' % (num1, num2, add(num1, num2)))
# Test for 'subtract' option.
elif option == '2':
    num1, num2 = numbers()
    print('%f - %f = %f' % (num1, num2, subtract(num1, num2)))
# Fallback for when no supported option is selected.
else:
    print("Invalid input, please choose '1' or '2'.")