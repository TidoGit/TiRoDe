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

#def calc_exp(x,y):
#    total = x ** y
#    return total

#option menu
while True:
    print("Option menu \n")
    print(12 * "=")
    print("1. add")
    print("2. minus")
    print("3. multiply")
    print("4. divide")
    print("5. quit")


    answer = input("Please make a choice:\n")
    x = float(input("Enter a number: \n"))
    y = float(input("Enter a number: \n"))

    if answer == "1":
        print("\nCalculating %.2f + %.2f" %(x, y))
        print("Answer: " + str(calc_add(x,y)))
        print("\n \n")
    elif answer == "2":
        print("\nCalculating %.2f - %.2f" %(x, y))
        print("Answer: " + str(calc_minus(x,y)))
        print("\n \n")
    elif answer == "3":
        print("\nCalculating %.2f * %.2f" %(x, y))
        print("Answer: " + str(calc_multiply(x,y)))
        print("\n \n")
    elif answer == "4":
        print("\nCalculating %.2f / %.2f" %(x, y))
        print("Answer: " + str(calc_divide(x,y)))
        print("\n \n")
    elif answer == "5":
        print("\nBye Bye")
        break
    else:
        print("\n Sorry i didn't catch that, try again \n \n")
        continue