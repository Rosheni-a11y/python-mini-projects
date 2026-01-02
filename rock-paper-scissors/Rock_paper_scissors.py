import random

choices = ["rock","paper","scissors"]

player_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors! \n")

while True:
  player = input("Choose (rock/paper/scissors): ").lower()

  if player not in choices:
    print("Invalid choice! Try again\n")
    continue

  computer = random.choice(choices)
  print(f"Computer chose: {computer}")

  if player == computer:
    print("It's a tie!")
  elif (player == "rock" and computer == "scissors") :
       (player == "paper" and computer == "rock") 
       (player == "scissors" and computer == "paper")
       print("You win this round!")
       player_score += 1

  else:
     print("Computer wins this round! ")
     computer_score +=1

  print(f"Score - You: {player_score} | Computer: {computer_score}\n")
  
  play_again = input("Play again? (yes/no)").lower()
  if play_again != "yes":
     print(f"Final Score You: {player_score} | Computer: {computer_score}")
     if player_score >computer_score:
        print("You Won! Congrats!")
     elif computer_score > player_score:
        print("Computer Won! Better luck next time!")
     else:
        print("It's a tie overall")
     print("\nThanks for playing!")
     break