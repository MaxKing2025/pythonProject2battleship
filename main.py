
# random use for G.L selecting target and placing ships

import random
ranint = random.randint(0,10)
print (ranint)


rows = 25
cols = 25

#make the gl board
board = [["~" for i in range (cols)]for j in range (rows)]

print("    0    1    2    3    4")
for i in range (0,5):
    print(i,board[i])

# only odd boats total 6 === three 3s == two 5s == one 7
xinput = int(input("give me x"))
yinput = int(input("give me y"))
axis = input("L/R or U/O")
print("you picked "+ axis)

def three_boat ():
    # only odd boats total 6 --- three 3s -- two 5s -- one 7
    ran_dir = random.randint(0,1)
    xinput = random.randint(3,12)
    yinput = random.randint(3,12)

    if ran_dir == 1:
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1] = "B"
    else:
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"
    if axis == "U" or axis == "D" or axis == "U/D" or axis == "u" or axis == "d":
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"
    else:
        board[xinput][yinput] = "B"
        board[xinput + 1] [yinput] = "B"
        board[xinput][yinput - 1] = "B"

three_boat ()
three_boat ()

for i in range (0,4):
    print(i, board[i])

three_boat ()
print_gl_board()
three_boat ()
print_gl_board()

for small_coor in range(0,3):
    #ran_int = random.randint(1,  11)
    lst[xinput][yinput] = "0"

print("    0    1    2    3    4")
for i in range (0,5):
    print(i,board[i])

elif: x == "X" or (boar =="O") :
    print("hit")







