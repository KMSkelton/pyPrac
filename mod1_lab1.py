'''
Create a python script called "hw1.py"
This script should contain:

Ask the user three original questions and store their input as variables
Combine the three answers into a sentence of your choosing
Print out the final combined sentence using one of the string operations
Add docstrings and comments to your code

'''

def dinnerQuiz():
    food = input('What is the last thing you ate? ')
    cost = float(input('How much did that cost? '))
    enjoy = input('Did you enjoy that? (y/n) ')

    if enjoy == 'n':
        print('That\'s too bad! ${:.2f} is too much to spend on {}, especially if you didn\'t enjoy it'.format(cost, food))
    else:
        print('That\'s excellent! ${:.2f} is a great price for {}'.format(cost, food))

dinnerQuiz()