'''
This is simple calculator that computes two numbers entered by the user
And performs the math operation entered before
'''


def get_first_num():
    '''
     First number entered must be an integer
    '''

    while True:
        try:
            num1 = float(input('Enter first number: '))
        except ValueError:
            print('Input is not an number, please try again')
            continue
        else:
            return num1
            break


def get_second_num():
    '''
    Second number entered must be an integer
    '''
    while True:
        try:
            num2 = float(input('Enter second number: '))
        except ValueError:
            print('Input is not an number, please try again')
            continue
        else:
            return num2
            break


def answer():
    print('-----------------------------------------------')
    print('The answer is ' + result)


while True:
    print('-----------------------------------------------')
    print('Options:')
    print('\tEnter \'add\' to add two numbers')
    print('\tEnter \'subtract\' to subtract two numbers')
    print('\tEnter \'multiply\' to multiply two numbers')
    print('\tEnter \'divide\' to divide two numbers')
    print('\tEnter \'modulo\' to get the remainder of two numbers')
    print('\tEnter \'floor\' to get the floor division of two numbers')
    print('\tEnter \'exponent\' to raise the first number to the power of the second')
    print('\tEnter \'quit\' to end the program')
    print('\nNote: symbols can also be used')
    print('-----------------------------------------------')
    user_input = input(':')

    if user_input == 'quit':
        break
    elif user_input == 'add' or user_input == '+':
        a = get_first_num()
        b = get_second_num()
        result = str(a + b)
        answer()
    elif user_input == 'subtract' or user_input == '-':
        a = get_first_num()
        b = get_second_num()
        result = str(a - b)
        answer()
    elif user_input == 'multiply' or user_input == '*':
        a = get_first_num()
        b = get_second_num()
        result = str(a * b)
        answer()
    elif user_input == 'divide' or user_input == '/':
        a = get_first_num()
        b = get_second_num()
        try:
            result = str(a / b)
            answer()
        except ZeroDivisionError:
            print('Error due to dividing by zero')
    elif user_input == 'modulo' or user_input == '%':
        a = get_first_num()
        b = get_second_num()
        try:
            result = str(a % b)
            answer()
        except ZeroDivisionError:
            print('Error due to dividing by zero')
    elif user_input == 'floor' or user_input == '//':
        a = get_first_num()
        b = get_second_num()
        try:
            result = str(a // b)
            answer()
        except ZeroDivisionError:
            print('Error due to dividing by zero')
    elif user_input == 'exponent' or user_input == '**':
        a = get_first_num()
        b = get_second_num()
        result = str(a ** b)
        answer()
    else:
        print('Unknown input')
