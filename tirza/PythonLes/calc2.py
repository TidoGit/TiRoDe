'''
Advanced calculator
use functions to add options
add option menu
'''

#calculator functons
def calc_add(x,y):
    total = x + y
    return total

def calc_minus(x,y):
    total = x - y
    return total    

def calc_multiply(x,y):
    total = x * y
    return total

def calc_divide(x,y):
    total = x / y
    return total

def calc_exp(x,y):
    total = x ** y
    return total

while True:
    print("Option menu \n")
    print(12 * "=")
    print("1. add")
    print("2. minus")
    print("3. multiply")
    print("4. divide")
    print("5. exponent")


    answer = input("Please make a choice:\n")
    x = float(input("Enter a number: \n"))
    y = float(input("Enter a number: \n"))

    if answer == "add" or "1":
        print("Calculating " + x  + "+" + y )
        print("Answer: " + str(calc_add(x,y)))
    elif answer == "minus" or "2":
        print("Answer: " + str(calc_minus(x,y)))
    elif answer == "multiply" or "3":
        print("Answer: " + str(calc_multiply(x,y)))
    elif answer == "divide" or "4":
        print("Answer: " + str(calc_divide(x,y)))
    elif answer == "exponent" or "5":
        print("Answer: " + str(calc_exp(x,y)))
