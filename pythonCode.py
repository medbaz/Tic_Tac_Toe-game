import random 
from random import randint as rino
from math import ceil
import copy
import pprint
# decimal = bin(20) 
# binary = "10100"
# number = int(binary, 2)
# print(decimal)
# print(number)

"""
def function(decimal) :
    dicimalArray = list(decimal)
    dicimalArray.reverse()
    deciToNumber = 0
    index = 0
    print(dicimalArray)
    for i  in dicimalArray:
        if i != '0' and i != '1':
            print("please enter a valide binary number ")
            break
        deciToNumber += pow(2,index) * int(i)
        index += 1
    print(deciToNumber)
"""


# addDeci = input("please enter a decimal number ")
# function("010111")
# a = bin(10)
# b = bin(-11)

# print(a)
# print(b)
# print(~10)
# "00001011"

# number = '45'
# typeOfValue = type(number)
# print(typeOfValue)

# age = 20
# while age > 2 :
#     input("please type your name " )
#     age -= 1

# for i in str(12345) :
#     print(rino(1,9))
# print(abs(-44))



""" 
def dividByName(divide) :
    try :
        return 5/divide
    except ZeroDivisionError:
        print("an error has occured ")

dividByName(0)
"""


"""
spam = ['cat','holam','cat','ants', 'cats', 'dogs', 'badgers', 'elephants','Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
name , age  = spam[0:2]
spam.insert(1,"hologram")
print(spam.count('cat'))
print(spam[1])
spam.sort(key=str.lower)
print(spam)
"""


"""
spam = {'color': 'red', 'age': 42}
for i in spam.values() :
    print(i)

dictKeys = spam.items()
listLIKE = list(dictKeys)
theList = copy.deepcopy(listLIKE)
print(theList)
# del theList[0]
# print(('age', 42) in theList)
"""



"""
for i  in range(len(theList)) :
    theList[i]=list(theList[i])
print(theList)
"""
"""
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(pprint.pformat(count))
"""



theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''}

boardKeys = list(theBoard.keys())
for i in range(len(theBoard)):
    if theBoard[boardKeys[i]] == '':
        theBoard[boardKeys[i]] = i + 1


def drawBoard() :
    count = 0
    for i in theBoard :
        print(theBoard[i] ,end="")
        count += 1
        if count%1 == 0 and count != 3 and count != 6 and count != 9:
            print(" | ",end='')
        if count%3 == 0 and count <= 6:
            print()
            print("- + - + - ")

drawBoard()
print()
print("choose number between 1-9")


O_Success = True
X_Success = True

def o_input() :
    global O_Success
    global X_Success
    oLocation =  input("Player 1 (O)  place your O : ")

    if  int(oLocation) <= 9 and int(oLocation) >= 1 and theBoard[boardKeys[int(oLocation)-1]] != "O" and theBoard[boardKeys[int(oLocation)-1]] != "X"  :
        theBoard[boardKeys[int(oLocation)-1]] = "O"
        drawBoard()
        print()
        O_Success = False
        X_Success = True
    else:
        print("already full choose another number ")
    
    return oLocation


def x_input() :
    global O_Success
    global X_Success
    oLocation =  input("Player 2 (X)  place your X : ")

    if  int(oLocation) <= 9 and int(oLocation) >= 1 and theBoard[boardKeys[int(oLocation)-1]] != "O" and theBoard[boardKeys[int(oLocation)-1]] != "X"  :
        theBoard[boardKeys[int(oLocation)-1]] = "X"
        drawBoard()
        print()
        X_Success = False
        O_Success = True
    else:
        print("already full choose another number ")
    return oLocation



no_Win = False
while no_Win  :

    
    currentPlayer = ''
    if O_Success == True :
        o_input()
        currentPlayer = "O"
    elif X_Success == True :
        x_input()
        currentPlayer = "X"
    boardList = list(theBoard.items())
    
    all_Top_values = [value for key , value in theBoard.items()  if key.startswith('top')]
    all_Mid_values = [value for key , value in theBoard.items()  if key.startswith('mid')]
    all_Low_values = [value for key , value in theBoard.items()  if key.startswith('low')]

    all_L_values = [value for key , value in theBoard.items()  if key.endswith('L')]
    all_R_values = [value for key , value in theBoard.items()  if key.endswith('R')]
    all_M_values = [value for key , value in theBoard.items()  if key.endswith('M')]


    if len(set(all_Top_values)) == 1 or len(set(all_Mid_values)) == 1 or len(set(all_Low_values)) == 1 :
        no_Win = False
        print(currentPlayer , " is the winner ")
        break

    if len(set(all_L_values)) == 1 or len(set(all_R_values)) == 1 or len(set(all_M_values)) == 1 :
        no_Win = False
        print(currentPlayer , " is the winner ")
        break

    if theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] :
        no_Win = False
        print(currentPlayer , " is the winner ")
        break
    if theBoard['low-L'] == theBoard['mid-M'] == theBoard['top-R'] :
        no_Win = False
        print(currentPlayer , " is the winner ")
        break

for i in theBoard :
    array = i.split('-')
    all_Top_values = [value for key , value in theBoard.items()  if key.startswith('top')]
    print(array)

    