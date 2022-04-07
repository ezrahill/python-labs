import random
import time
import ascii_art        # Import the ASCII_ART.PY File

# Terminal colours - Thanks to https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to ask the user the question
def quest():
    while True:
        try:
            a = int(input(f'What is the missing number: {num} x _ = {q} ? ' + bcolors.ENDC))
            if a or a == 0:
                # if it was equal - break from the while loop
                break
        except ValueError:
            print(bcolors.FAIL + '\nPlease enter a number\n' + bcolors.ENDC)

    cal(a)

# Function to calculate the answer
def cal(a):
    global tries
    tries += 1
    if num * int(a) == q:
        print(bcolors.OKGREEN + f'\nWell done, {num} x {a} = {q}\n' + bcolors.ENDC)

    else:
        print(bcolors.WARNING + '\nSorry, that is the wrong answer, try again?\n' + bcolors.ENDC)
        global incorrect
        missing = q // num
        incorrect.append(f'You entered: {num} x {a} = {q}, the correct answere is: {num} x {missing} = {q}')
        quest()

#### START ####
# Ask for the users name and store in name variable
name = input("Hey, what is your name? " )

# Check name for a value and print some ASCII art
if name.capitalize() == 'Amya':
    ascii_art.print_girl()
elif name.capitalize() == 'Lathan':
    ascii_art.print_boy()
else:
    ascii_art.print_other()

# Print greeting
print("\nNice to meet you " + bcolors.HEADER + name.capitalize() + bcolors.ENDC + ", lets get started!\n")

# 1 Second delay
time.sleep(1)

# The range of times tables to test
choice_range = list(range(1,13))

# Ask user what they want testing on and break from the loop if a number between 1-12 is entered
while True:
    try:
        test_num = int(input("Which times table would you like testing on [1-12]? : "))
        if test_num in choice_range:
            break
        else:
            print(bcolors.FAIL + '\nPlease enter a number between 1 - 12\n' + bcolors.ENDC)
    except ValueError:
        print(bcolors.FAIL + '\nPlease enter a number between 1 - 12\n' + bcolors.ENDC)

# Print the users selection
print(f'\nAwesome, let the {test_num} times testing begin...\n')

# Covert users string selection to an integer
num = int(test_num)

# Generate a list of answers for the given times table
tt = list(range(0,145,num))[:12]

# Variables to keep score
correct = 0
tries = 0
incorrect = []

# Loop until 10 correct answers
while correct < 10:
    q = random.choice(tt)       # Pick a random answer
    tt.remove(q)                # Remove the random answer from the list
    quest()                     # Call the quest function
    correct += 1                # Increase correct variable by 1
    
    # Check score and output to user
    if correct == 1:
        print(f'You have {correct} point, you need 10 to complete the game, keep going!\n')
    elif correct <= 9:
        print(f'You have {correct} points, you need 10 to complete the game, keep going!\n')
    else:
        ascii_art.print_gratz()

        pass_mark = round(correct / tries * 100)
        if pass_mark >= 80:
                    print(bcolors.UNDERLINE + "AMAZING WORK " + bcolors.HEADER + name.upper() + bcolors.ENDC + bcolors.UNDERLINE + " YOU ARE SUPER SMART!\n" + bcolors.ENDC)
        print(f'You have {correct} points, and you have completed the test with a score of {pass_mark}%\n')
        if incorrect:
            print('You never got these right first time, make sure you remember them for next time!\n')
            incorrect = list(dict.fromkeys(incorrect))
            for ans in incorrect: print(ans)
