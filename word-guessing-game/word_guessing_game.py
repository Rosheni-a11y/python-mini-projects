import random

word_bank = ["hello", "world", "yellow","game","programming"]


word = random.choice(word_bank)

guessword = ["_"] * len(word)

attempts = 10

print("Welcome to word guessing game!")

while attempts > 0:
  print("\nWord:", ' '.join(guessword))
  print("Attempts left:", attempts)

  guess = input("Guess a letter: ").lower()

  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        guessword[i] =guess
    print("Great Guess!")

  else:
    attempts -=1
    print("Wrong guess! Attempts left: " + str(attempts))

  if "_" not in guessword:
    print("Congratulations! You guessed the word: " + word)
    break
  
  if attempts == 0 and "_" in guessword:
    print("You run out of attempts! The word was: " + word)