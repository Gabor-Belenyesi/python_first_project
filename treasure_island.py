while True:
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.") 
  

  player_answer = input("Where do you want to go on the mainland? To the forest: 'Left' or, to the shore? : 'Right' ")
  
  if player_answer.lower() == "left":
    player_second_answer = input("There is an island close to you. You want to 'swim' or 'wait' to the boat? ")
    if player_second_answer == "swim":
      player_second_answer = input("A hungry shark catched you! Game Over! You wanna try again? 'Y' or 'N' ")
      if player_second_answer.upper() == "Y":
        continue
      else:
        print("Bye!")
        break
    elif player_second_answer == "wait":
      print("You find a house on the island, you have to choose a door, which is hiding a treasure.")
      player_third_answer = input("Which door do you want to go through? 'red', 'blue', or 'yellow'? ")
      if player_third_answer == "yellow":
        print("You find the treasure!")
        break
      else:
        last_answer = input("You find a burning room. Game Over! You wanna try again? 'Y' or 'N' ")
        if last_answer.upper() == "Y":
          continue
        else:
          print("Bye!")
          break
    else:
      print("Wrong answer!")
      
  else:
    print("In the forest a hungry beast ate you.")
    print("Game over!")
    last_question = input("You wanna try again? 'Y' or 'N' ")
    if last_question.upper() == "Y":
      continue
    else:
      print("Bye!")
      break
    