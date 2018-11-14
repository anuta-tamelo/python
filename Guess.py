
import random

print('Hello! What is your name?')
myName = input()

print ('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

number = random.randint(1, 20)

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print ('Your guess is too low.')
    elif guess > number:
        print ('Your gues is too high.')
    else: #guess == number:
        print ('Good job, ', myName, '! You guessed my number in ', guessesTaken, ' guesses!')
        break
else:
    print ('Nope. The number I was thinking of was ', number, '.')