name = input("Hello! What's your name? ")
name = name.title()
age = input("Hello %s! What's your age? " % name)

print('So, your name is %s and you are %s years old!' % (name, int(age)))