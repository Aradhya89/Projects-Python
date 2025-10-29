import numpy as np
import os
import random
import tabulate as tb


"""
array should look like this
[[x,x,o],
[o,x,o]
[x,x,x]]

"""


def playable(arr,choice):
    position = np.where(arr == choice)
    if position[0].size == 0:
        return False
    else:
        return True
    

def computer_chance(arr):
    com_choice = str(random.randint(1,10))
    while not playable(arr,com_choice):
        com_choice = str(random.randint(1,10))

        # code to break while loop when there is no playable element is left
        if not np.any(np.isin([str(a) for a in range(1,10)] , arr)):
            break
        
    arr[arr == com_choice] = "O"
    return (f"COMPUTER PLAY AT {com_choice}")



def player_chance(arr):
    choice = input("ENTER THE POSITION WHERE YOU WANT TO ENTER THE PLAY :")

    # to get a playable position
    while not playable(arr, choice):

        print("CAN'T PLAY THERE")
        choice = input("ENTER THE POSITION WHERE YOU WANT TO ENTER THE PLAY :")


    #work if playable
    arr[arr == choice] = "X"
    
# function to print all the data in tabule format
def printing(arr):
    print(tb.tabulate(arr,tablefmt='grid'))
    

# function to clear terminal
def clrscr():
    os.system("cls")


def checking(arr):

    #adding all the column and rows
    column = arr[0]+arr[1]+arr[2]
    row = arr[:,0]+arr[:,1]+arr[:,2]

    # adding all the diagonals
    diagonal = "".join(np.diagonal(arr))
    reverse_daigonal = "".join(np.diagonal(np.flip(arr,axis = 0)))

    # gathering all the combination in one array
    possible_combintaion = np.concatenate((column,row,np.array([diagonal,reverse_daigonal])))

    # print(possible_combintaion) #for debugging

    # checking win or lose
    if "XXX" in possible_combintaion:
        return 1
    elif "OOO" in possible_combintaion:
        return -1
    elif not np.any(np.isin([str(a) for a in range(1,10)] , arr)):
        return 0

# function just to reduce code
def frontend_part(arr,cc):
    clrscr()
    print(cc)
    outputARR = np.array(arr,dtype='<U20',copy= True)
    # red ="\033[91m"
    # yellow ="\033[93m"
    # end = "\033[0m"
    #bold = "\033[1m"
    outputARR[outputARR == "X"] = "\033[1m\033[91mX\033[0m"
    outputARR[outputARR == "O"] = "\033[1m\033[93mO\033[0m"
    printing(outputARR)


# main function
arr = np.array( [str(a) for a in range(1,10)] , dtype= str ).reshape(3,3)
cc = ''

while True:

    frontend_part(arr,cc)
    player_chance(arr)
    print("DONE SINCE PLAYER CHANCE")

    cc = computer_chance(arr)


    if checking(arr) == 1:
        frontend_part(arr,cc)
        print("YOU WIN")
        break


    elif checking(arr) == -1 :
        frontend_part(arr,cc)
        print("YOU LOSE")
        break


    elif checking(arr) == 0:
        frontend_part(arr,cc)
        print("DRAW")
        break




