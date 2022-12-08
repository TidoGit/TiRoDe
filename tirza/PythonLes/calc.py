'''When the script runs, use input() three seperate times to:
   Ask for the type of operation (add or subtract)
   Ask for the first number. This should support floats too.
   Ask for the second number. This should support floats too.
   Calculate the addition or subtraction entered by the user and print the result.
   Don't simply print the result, also print the operation and numbers 
   (replace <OPERATION> with + or - )
'''
#start of calculator
print("Calculator")
#user input
operation = input("add or substract? \n")
num1 = float(input("Enter first number: \n"))
num2 = float(input("Enter second number: \n"))
#Calculate the addition or subtraction entered by the user and print the result.
if operation == "add":
    action = num1 + num2
    print("The answer: %.2f + %.2f = %.2f" %(num1, num2, action))
elif operation == "substract":
    action = num1 - num2
    print("The answer: %.2f - %.2f = %.2f" %(num1, num2, action))

#end 