
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

winner=None
gamerunning=True
currentplayer='X'

#PRINT BOARD

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print(board[6] + " | " + board[7] + " | " + board[8] )

#taking input from user

def takeinput(board):
    while True:
        if currentplayer=='X':
            inp=int(input('Enter the number (1-9) Player X  = '))
        else:
            inp = int(input('Enter the number (1-9) Player O = '))
        if inp<=9 and inp>=1 and board[inp-1]=="-":
            board[inp-1]=currentplayer
            break
        else:
            if currentplayer=='X':
                print("opps the number is already taken Player X")
            else:
                print("opps the number is already taken Player O")
            printboard(board)


#check for win
def checkrow(board):
    global winner
    if(board[0]==board[1]==board[2] and board[0]!="-") or(board[3]==board[4]==board[5] and board[3]!="-") or (board[6]==board[7]==board[8] and board[8]!="-"):
        winner=currentplayer
        return True

def checkcolum(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (
            board[1] == board[4] == board[7] and board[1] != "-") or (
            board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentplayer
        return True

def checkdiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentplayer
        return True

def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It's a tie")
        gamerunning= False

def checkwin():
    if checkcolum(board) or checkrow(board) or checkdiagonal(board):
        print(f"Thw winner is : {winner}")

def switchplayer():
    global currentplayer
    if currentplayer=='X':
        currentplayer='O'
    else:
        currentplayer='X'



while gamerunning:
    printboard(board)
    if  winner!=None:
        break
    takeinput(board)
    checkwin()
    checktie(board)
    switchplayer()






