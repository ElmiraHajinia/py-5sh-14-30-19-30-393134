""" بازی دوز (Tic-Tac-Toe)
 صفحه بازی ۳ در ۳
بازی دو نفره
تشخیص برنده
تشخیص مساوی شدن بازی"""

from micro import*
player="X"
for i in range(9):
    while True:
        position=int(input("enter your position from 0-8==="))
        if position<0 or position>8:
            print("wrong number")
            continue
        if GameBoard[position]==" ":
            player=posiiition(position,player)
            break
        else:
            print("choose another position")    

print(*GameBoard[0:3],sep=" | ")
print(*GameBoard[3:6],sep=" | ")
print(*GameBoard[6:9],sep=" | ")

if GameBoard[0] and GameBoard[1] and GameBoard[2]=="X":
    print("winner==X")
elif GameBoard[0] and GameBoard[1] and GameBoard[2]=="O":
    print("winner==O")
elif GameBoard[3] and GameBoard[4] and GameBoard[5]=="X":
    print("winner==X")
elif GameBoard[3] and GameBoard[4] and GameBoard[5]=="O":
    print("winner==O")
elif GameBoard[6] and GameBoard[7] and GameBoard[8]=="X":
    print("winner==X")
elif GameBoard[6] and GameBoard[7] and GameBoard[8]=="O":
    print("winner==O")
elif GameBoard[0] and GameBoard[3] and GameBoard[6]=="X":
    print("winner==X")
elif GameBoard[0] and GameBoard[3] and GameBoard[6]=="O":
    print("winner==O")
elif GameBoard[1] and GameBoard[4] and GameBoard[7]=="X":
    print("winner==X")
elif GameBoard[1] and GameBoard[4] and GameBoard[7]=="O":
    print("winner==O")
elif GameBoard[3] and GameBoard[6] and GameBoard[8]=="X":
    print("winner==X")
elif GameBoard[3] and GameBoard[6] and GameBoard[8]=="O":
    print("winner==O")
elif GameBoard[0] and GameBoard[4] and GameBoard[8]=="X":
    print("winner==X")
elif GameBoard[0] and GameBoard[4] and GameBoard[8]=="O":
    print("winner==O")    
elif GameBoard[2] and GameBoard[4] and GameBoard[6]=="X":
    print("winner==X")
elif GameBoard[2] and GameBoard[4] and GameBoard[6]=="O":
    print("winner==O")
else:
    print("It a draw, no winner")    