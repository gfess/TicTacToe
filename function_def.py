#this will define the functions used in the main

import random
#letting the user know what the game is and how to play
def Welcome():
  print("Welcome to Tic-Tac-Toe!\n How to play:\n Choose an X or O to place on the board. \n Each player will take turns marking their letter in a space on   a 3x3 grid. \n To win you must place 3 of your letters in a horizontal, vertical or diagonal row.")

#This function will prompt the user to pick either an X or an O to start the game with
def pickLetter():
  letter = raw_input("Select your letter(X or O):")
  while not("X" in letter or "O" in letter):
      print("That is not a valid move! Enter either X or O. Please try again")
      letter = raw_input("Select your letter(X or O):")
  return letter

#this function will call the printBoard function while adding index to it's list parameters
def createBoard():
   board = ["1","2","3","4","5","6","7","8","9"]
   return board

#this function will create the board by calling on the create board function
def printboard(board):
   print(" ",board[0],"|",board[1],"|",board[2])
   print("-----------------")
   print " ", board[3], " | ", board[4], " | ", board[5]
   print "-----------------"
   print " ", board[6], " | ", board[7], " | ", board[8]
   pass

#This function will take the users chosen letter from pickletter and then will prompt the user to choose a location between 1-9 on the board
def getInput(letter,board):
   place = int(input("Where would you like to place " + letter + " (1-9)?")) - 1
   while True:
      if place < 0 or place > 8:
          print("This is not a valid move. Please choose a value between 1-9.")
          place = int(input("Where would you like to place " + letter + " (1-9)?")) - 1
      else:
          break
   while ("X" in board[place] or "O" in board[place]):
      print("Invalid move! Location is already taken. Please try again.")
      place = int(input("Where would you like to place " + letter + " (1-9)?")) - 1
      while True:
          if place < 0 or place > 8:
              print("This is not a valid move. Please choose a value between 1-9.")
              place = int(input("Where would you like to place " + letter + " (1-9)?")) - 1
         else:
             break
   board.pop(place)
   board.insert(place,letter)
   return board, letter

#the following functions will check each row/columns/diagonals of the board looking for trues or falses. if there is no winner, the function will be passed
def checkRows(letter,board):
   if (letter in board[0] and letter in board[1] and letter in board[2]):
       return True
   elif (letter in board[3] and letter in board[4] and letter in board[5]):
       return True
   elif (letter in board[6] and letter in board[7] and letter in board[8]):
       return True
   else:
       pass
def checkCols(letter,board):
   if (letter in board[0] and letter in board[3] and letter in board[6]):
       return True
   elif (letter in board[1] and letter in board[4] and letter in board[7]):
       return True
   elif (letter in board[2] and letter in board[5] and letter in board[8]):
       return True
   else:
       pass
def checkDiags(letter,board):
   if (letter in board[0] and letter in board[4] and letter in board[8]):
       return True
   elif (letter in board[2] and letter in board[4] and letter in board[6]):
       return True
   else:
       pass
 
#This function will check to see if there is a winner
def checkWin(letter,win_status):
   if win_status == True:
      print(letter," has won Tic-Tac-Toe!")
   else:
      pass

#This function will prompt the user to choose if they want to play against a computer or another player
def pickOpponent():
   opponent = int(input("Do you want to play with (1) computer or (2) player? (select 1 or 2) ")
   while opponent > 2 or opponent < 1:
      print("Have to select (1) computer or (2) player. Please try again.")
      opponent=input("Do you want to play with (1) computer or (2) player? (select 1 or 2) ")
   return opponent
  
#This function is the same as getInput but for the "computer"
#importing random dict to randomize numbers
def computer(letter,board):
   print("Computer Turn:")
   place = random.randint(1,9) - 1
   while ("X" in board[place] or "O" in board[place]):
      place = random.randint(1,9) - 1
   board.pop(place)
   board.insert(place,letter)
   return board, letter




      
