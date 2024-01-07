import random
import string   # import class of strings
from words import words

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangMan():
    word = getValidWord(words)
    # Letters in the word
    wordLetters = set(word)

    # Upper case strings
    alphabet = set(string.ascii_uppercase)

    # Keep track of what the user has guessed
    usedLetters = set()

    # Getting user input
    while len(wordLetters) > 0:

    # Letting user know of used letters
    # " ".join(['a' , 'b', 'cd']) ---> 'a b cd'
        print("You have used these letters: " ," ".join(usedLetters)) 

    # what the current word is ie. W - R D
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current word: ' , ' '.join(wordList))

        userLetter = input("Guess a letter: \n").upper() 
        print (" ")

        if userLetter in alphabet - usedLetters:

            if userLetter in wordLetters:
                usedLetters.add(userLetter)
                wordLetters.remove(userLetter)

            else:
                print('Incorrect guess! Try again \n') 
    
        elif userLetter in usedLetters:
            print(" You have already used that letter. Please try again")

        else:
            print("Invalid character")

    print("You have won the game!!!")

hangMan()