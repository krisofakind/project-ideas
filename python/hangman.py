import random

def play_hangman():
  # Choose a random word from a list of words
  words = ["apple", "banana", "orange", "strawberry", "grape"]
  word = random.choice(words)
  # Initialize variables
  lives = 6
  guessed_letters = []
  # Set up the word with underscores for unguessed letters
  word_display = ["_"] * len(word)

  while lives > 0:
    # Print the current state of the game
    print("Current word: ", " ".join(word_display))
    print("Lives remaining: ", lives)
    print("Guessed letters: ", " ".join(guessed_letters))
    # Get the player's next guess
    guess = input("Guess a letter: ")
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid guess. Please enter a single letter.")
      continue
    # Check if the letter has already been guessed
    if guess in guessed_letters:
      print("You already guessed that letter. Try again.")
      continue
    # Add the letter to the list of guessed letters
    guessed_letters.append(guess)
    # Check if the letter is in the word
    if guess in word:
      # Update the word display with the correct guess
      for i in range(len(word)):
        if word[i] == guess:
          word_display[i] = guess
      # Check if the player has won
      if "_" not in word_display:
        print("Congratulations, you won! The word was: ", word)
        return
    else:
      # The guess was incorrect, so the player loses a life
      lives -= 1
  # The player has run out of lives, so they lose the game
  print("Sorry, you lost. The word was: ", word)

# Start the game
play_hangman()
