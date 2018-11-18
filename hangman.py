import random

words = {'Animals':'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(), 
         'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triange rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry'.split(),}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

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
    print ('H A N G M A N')

    global HANGMAN_PICS
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
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

    difficulty = None

    while not difficulty or difficulty not in 'EMH':
        print('Enter difficulty: E - easy, M - medium, H - hard')
        difficulty = input().upper()
        if difficulty == 'M':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
        if difficulty == 'H':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            del HANGMAN_PICS[5]
            del HANGMAN_PICS[3]

    global missedLetters
    missedLetters = ''

    global correctLetters
    correctLetters = ''

    global secretWord
    global secretSet
    secretWord, secretSet = getRandomWord(words)

    global gameIsDone
    gameIsDone = False
    

def isManHung(missedLetters):
    return len(missedLetters) == len(HANGMAN_PICS) - 1

resetGameState()

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