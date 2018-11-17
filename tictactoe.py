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

    return ['X', 'O'] if letter == 'X' else ['O', 'X']

def whoGoesfirst():
     return 'computer' if random.randint(0, 1) == 0 else 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, party):
    return (
        (board[7] == party and board[8] == party and board[9] == party) or 
        (board[4] == party and board[5] == party and board[6] == party) or 
        (board[1] == party and board[2] == party and board[3] == party) or 
        (board[7] == party and board[4] == party and board[1] == party) or 
        (board[8] == party and board[5] == party and board[2] == party) or 
        (board[9] == party and board[6] == party and board[3] == party) or 
        (board[7] == party and board[5] == party and board[3] == party) or 
        (board[9] == party and board[5] == party and board[1] == party)
    )

def getBoardCopy(board):
    return list(board)

def isSpaceFree(board, move):
    return board[move] == EMPTY

def getPlayerMove(board):
    while True:
        print('What is your next move? (1-9)')
        move = input()
        if move in '123456789':
            move = int(move)
            if isSpaceFree(board, move): return move

def chooseRandomMove(board, movesList):
    possibleMoves = [move for move in movesList if isSpaceFree(board, move)]
    return random.choice(possibleMoves) if possibleMoves else None

def canWin(board, move):
    if isSpaceFree(board, move):
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerLetter, move)
        return isWinner(boardCopy, computerLetter)
    
    return False

def getComputerMove(board, computerLetter):
    for cell in range(1, 10):
        if canWin(board, cell):
                return cell

    #move = next((cell for cell in range(1, 10) if canWin(board, cell)), None)
    #if move: return move

    move = chooseRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMove(board, [2, 4, 6, 8])

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





















