def main():
  Welcome()
  opponent = pickOpponent()
  UserLetter = pickLetter()
  if "X" in UserLetter:
    opponentLetter = "O"
  elif "O" in UserLetter:
    opponentLetter = "X"
  else:
    pass
  print("Please use the cell numbers between 1-9 to place your letter")
  print("The board will look like:")
  emptyBoard = createBoard()
  printBoard(emptyBoard)
  print("The empty board")
  board=[" "," "," "," "," "," "," "," "," "," "]
  printBoard(board)
  win_status = False
  cnt = 1
  while cnt < 10 and win_status == False:
    if cnt % 2 == 0:
      letter = "O"
    else:
      letter = "X"
    if opponent == 1:
      if "X" in letter and "X" in opponentLetter:
        computer(letter,board)
      elif "X" in letter and "X" in UserLetter:
        getInput(letter,board)
      elif "O" in letter and "O" in opponentLetter:
        computer(letter,board)
      elif "O" in letter and "O" in UserLetter:
        getInpu(letter,board)
      else:
        pass
    else:
      getInput(letter,board)
    while checkRows(letter,board)==True or checkCols(letter,board)==True or checkDiags(letter,board)==True:
      win_status = True
      checkWin(letter,win_status)
      break
    printBoard(board)
    cnt += 1
 if win_sstatus == False:
    print("There is a tie.")
 else:
    pass

if __name__ == '__main__':
  main()
      
    
        
