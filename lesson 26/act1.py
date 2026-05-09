board = {str(i): ' 'for i in range(1,10)}

def show():
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print("-+-+-")
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print("-+-+-")
    print(f"{board['1']}|{board['2']}|{board['3']}")

wins = [('7','8','9'),('4','5','6'),('1','2','3'),
('7','4','1'),('8','5','2'),('9','6','3'),
('7','5','3'),('1','5','9')]

turn = 'X'

for _ in range (9):
    show()
    move= input(f"{turn}move:")

    if board[move] ==' ': 
        board[move]= turn
    else:
        print("taken!")
        continue

    if any(board[a]== board[b] == board[c] != ' 'for a,b,c in wins):
        show()
        print(turn,"wins!")
        break

    turn = '0' if turn =='X' else 'X'
else:
    show()
    print("tie!")
    