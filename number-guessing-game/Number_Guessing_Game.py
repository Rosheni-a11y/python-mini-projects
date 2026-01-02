import random 

playing = True

while playing:
  secret_number= random.randint(1,50)
  guesses =0
  max_guesses = 5

  print("Welcome to Number Guessing Game!")
  print("I'm thinking of a number bewteen 1 and 50")
  print(f"You have  {max_guesses} guesses! ")

  while guesses < max_guesses:
    guess = int(input("Take a guess: "))
    guesses += 1

    if guess < secret_number:
      print(f"Too low! ({guesses}/{max_guesses} guesses used)")
    elif guess > secret_number:
      print(f"Too high! ({guesses}/{max_guesses} guesses used)")
    elif guess == secret_number:
      print(f"Congratulations! You guessed it in {guesses} guesses!")
      break
    else:
      print(f"You ran out of guesses! The number was {secret_number}")

  
  play_again = input("want to play again? (Yes/No)")
  if play_again.lower() != "yes":
    playing = False
    print("Thanks for playing! ")

        


