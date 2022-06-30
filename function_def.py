#this will define the functions used in the main

import random
#letting the user know what the game is and how to play
def Welcome():
  print("Welcome to Tic-Tac-Toe!\n How to play:\n Choose an X or O to place on the board. \n Each player will take turns marking their letter in a space on   a 3x3 grid. \n To win you must place 3 of your letters in a horizontal, vertical or diagonal row.")
 #This function will prompt the user to pick either an X or an O to start the game with
def pickLetter():
  letter = raw_input("Select your letter(X or O):")
  while not("X" in letter or "O" in letter):
      print(("That is not a valid move! Enter either X or O. Please try again")
      letter = raw_input("Select your letter(X or O):")
  return letter

#this function will call the printBoard function while adding index to it's list parameters
def createBoard():
   board = ["1","2","3","4","5","6","7","8","9"]
   return board
