import random

def  drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] +'|' + board[3])

def inputPlayerLetter():
    letter = None

    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesfirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or 
        (bo[4] == le and bo[5] == le and bo[6] == le) or 
        (bo[1] == le and bo[2] == le and bo[3] == le) or 
        (bo[7] == le and bo[4] == le and bo[1] == le) or 
        (bo[8] == le and bo[5] == le and bo[2] == le) or 
        (bo[9] == le and bo[6] == le and bo[3] == le) or 
        (bo[7] == le and bo[5] == le and bo[3] == le) or 
        (bo[9] == le and bo[5] == le and bo[1] == le)
    )

def getBoardCopy(board): return list(board)

def isSpaceFree(board, move): return board[move] == EMPTY

def getPlayerMove(board):
    move = None
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()

    return int(move)

def chooseMove(board, movesList):
    possibleMoves = [move for move in movesList if isSpaceFree(board, move)]

    return random.choice(possibleMoves) if possibleMoves else None


def getComputerMove(board, computerLetter):
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    move = chooseMove(board, [1,3,7,9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseMove(board, [2, 4, 6, 8])

def isBoardFull(board):
    return all([isSpaceFree(board,cell) for cell in range(1,10)])

EMPTY = ' '
PLAYER = 'player'
COMP = 'computer'
print('Welcome to Tic-Tac-Toe!')

while True:
    board = [EMPTY] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesfirst()
    print('The ', turn,' will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        letter = None
        gameOverMessage = None
        nextTurn = None
        move = None

        if turn == PLAYER:
            drawBoard(board)

            letter = playerLetter
            gameOverMessage = 'Hooray! you have won the game!'
            nextTurn = COMP
            move = getPlayerMove(board)
        else:
            letter = computerLetter
            gameOverMessage = 'The computer has beaten you. You lose.'
            nextTurn = PLAYER
            move = getComputerMove(board, computerLetter)

        makeMove(board, letter, move)

        if isWinner(board, letter):
          drawBoard(board)
          print(gameOverMessage)
          gameIsPlaying = False
        else:
            if isBoardFull(board):
                drawBoard(board)
                print('The game is a tie!')
                break
            else:
                turn = nextTurn

    print('Do you want to paly again? (yes or no)')
    if not input().lower().startswith('y'):
        break





















