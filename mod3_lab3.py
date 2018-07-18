'''
Guess that Animal!
Make a word guess game of your favorite animals.

Goal: A user must guess an animal name by guessing the letters in the name, one letter at a time.

Store an animal name in a variable
A user gets a number of guesses equal to 3 plus the length of the animal name
Use a while loop to get user input (guess a letter!) until they run out of guesses
Output the game status:  currently matching letters of the animal using a for loop
The game ends when they run out of guesses or when they guess the animal


Pseudocode

# make a variable with an animal name

# get the number of letters in the animal name (use len)

# set the number of guesses to be the animal name length plus 3

# use a while loop with a sentry variable to get user input

  # check if the letter is in the animal name

  # store the guessed letter in a list

  # increment the sentry variable

  # print out the status of the game using a for loop (go though the letters in the animal name and see if they're in the guess letter list

  # if all of the letters in the animal are in the guess letter list, break and congratulate the user

  # if the sentry variable is bigger or equal to the guesses, break and console the loser

'''

myAnimal = "yak"
myAnimalList = list(myAnimal)
# myAnimalList = []
# for letter in myAnimal:
#     myAnimalList.append(letter)
myAnimalSize = len(myAnimalList)
guessesAvail = myAnimalSize + 3
guessesUsed = 1
userGuessWrong = []
userGuessRight = []
print("Can you guess my favorite animal? You'll guess one letter at a time. Correct guesses will be capitalized.")

while guessesUsed <= guessesAvail:
    guessesLeft = guessesAvail - guessesUsed + 1

    userLetter = (input(f"What letter is in my favorite animal's common name? you have {guessesLeft} guesses remaining. "))
    if not userLetter in myAnimalList:
        userGuessWrong.append(userLetter)
        guessesUsed += 1
        print(f"Uh oh! '{userLetter}' is not in the name of my favorite animal. Try again!")
        print(f"So far you have guessed: wrong - {userGuessWrong} and right - {userGuessRight}.")
    if userLetter in myAnimalList:
        userGuessRight.append(userLetter)
        print(f"Great! '{userLetter}' is reqiured to spell my favorite animal.")
        if len(userGuessRight) == len(myAnimalList):
            print(f"Congratulations! I do love the {myAnimal}! It only took you {guessesUsed} guesses.")
            break
        print(f"So far you have guessed: wrong - {userGuessWrong} and right - {userGuessRight}.")
        guessesUsed += 1
if len(userGuessRight) != len(myAnimalList):
    print(f"Oh no! You didn't guess {myAnimal}. Better luck next time.")

