import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  O   |
      |
      |
     ===''','''
  +---+
  O   |
  |   |
      |
     ===''','''
  +---+
  O   |
 /|   |
      |
     ===''','''
  +---+
  O   |
 /|\  |
      |
     ===''','''
  +---+
  O   |
 /|\  |
 /    |
     ===''','''
  +---+
  O   |
 /|\  |
 /    |
     ===''','''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def getCurrentPicture(missedLetters):
    return HANGMAN_PICS[len(missedLetters)]

def printLine(string):
    for letter in string:
        print(letter, end=' ')
    print()


def displayBoard(missedLetters, correctLetters, secretWord):
    print(getCurrentPicture(missedLetters))
    print()

    print('Missed letters:', end=' ')
    printLine(missedLetters)

    blanks = ['_'] * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
           blanks[i] = secretWord[i]

    printLine(blanks)

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def resetGameState():
    global missedLetters
    missedLetters = ''

    global correctLetters
    correctLetters = ''

    global secretWord
    secretWord = getRandomWord(words)

    global gameIsDone
    gameIsDone = False
    

print ('H A N G M A N')
resetGameState()

def isManHung(missedLetters):
    return len(missedLetters) == len(HANGMAN_PICS) - 1

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        foundAllLetters = all(letter in correctLetters for letter in secretWord)

        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters += guess

        if isManHung(missedLetters):
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ', len(missedLetters), ' missed guesses and ',
                  len(correctLetters), ' correct guesses, the word was "', secretWord, '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            resetGameState()
        else:
            break




























     











