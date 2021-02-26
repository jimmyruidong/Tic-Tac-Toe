
defaultBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
player1marker = 'X'
player2marker = 'O'
currentmarker = 'X'

# defaultBoard2 = [[1,2,3],[4,5,6],[7,8,9]]
# def displayBoard2(board):
# Another way to make the board

def displayBoard(board):

    print(f'{board[1]}|{board[2]}|{board[3]}')

    print('-----')

    print(f'{board[4]}|{board[5]}|{board[6]}')

    print('-----')

    print(f'{board[7]}|{board[8]}|{board[9]}')

def markerPlacement(board, marker, num):
    board[num] = marker

def emptyLocation(board, position):
    if type(board[position]) == int:
        return True
    else:
        return False

def isDraw(board):
    for i in range(1,10):
        if emptyLocation(board, i):
            return False
    return True

def isWin(board, marker):
    if (board[7] == marker and board[8] == marker and board[9] == marker) \
            or (board[4] == marker and board[5] == marker and board[6] == marker) \
            or (board[1] == marker and board[2] == marker and board[3] == marker) \
            or (board[7] == marker and board[4] == marker and board[1] == marker) \
            or (board[8] == marker and board[5] == marker and board[2] == marker) \
            or (board[9] == marker and board[6] == marker and board[3] == marker) \
            or (board[7] == marker and board[5] == marker and board[3] == marker) \
            or (board[9] == marker and board[5] == marker and board[1] == marker):
        #Backslash - make things clear vs long long line
        return True
    else:
        return False

def reset():
    print("Play again? (Y/N)")
    if input().lower().startswith('y'):
        defaultBoard = [0,1,2,3,4,5,6,7,8,9]
        return True
    else:
        return False

def playerInput(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not emptyLocation(board, position):
        #If position is > 0 and position <10, much faster. Imagine if its a Go board.
        position = int(input(f"{currentmarker}'s turn, choose an empty position between 1-9: "))
        # displayBoard(defaultBoard)

    return position

def isPlay():
    play_game = input('Are you ready to play? Y/N.')

    if play_game.lower()[0] == 'y':
        return True
    else:
        return False

while True:

    print(player1marker + ' will go first.')

    if isPlay():
        isPlaying = True
    else:
        isPlaying = False

    while isPlaying:
# currentmarker == player1marker:

            displayBoard(defaultBoard)
            position = playerInput(defaultBoard)
            markerPlacement(defaultBoard, currentmarker, position)

            if isWin(defaultBoard, currentmarker):
                displayBoard(defaultBoard)
                print(f'{currentmarker} wins!')
                isPlaying = False
            else:
                if isDraw(defaultBoard):
                    displayBoard(defaultBoard)
                    print('The game is a draw!')
                    break
                else:
                    if currentmarker == player1marker:
                        currentmarker = player2marker

                    else:
                        currentmarker = player1marker

    if not reset():
        break