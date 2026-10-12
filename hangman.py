import random

# List of possible words
words = ["book", "vehicle", "enterprise", "bridge", "first"]

# Choose a random word
word = random.choice(words)

# Keep track of guessed letters
guessed_letters = []

# Keep track of incorrect guesses
incorrect_guesses = 0

# Game continues until the player makes 6 incorrect guesses
while incorrect_guesses < 6:

    # Build the word display
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Make sure the player enters one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the new guess to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Incorrect!")

    # Rebuild the display after the new guess
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    # Check if the player has guessed the entire word
    if "_" not in display_word:
        print(f"\nCongratulations! You guessed the word: {word}")
        break

# If the player reaches 6 incorrect guesses
if incorrect_guesses == 6:
    print(f"\nGame over! The word was: {word}")
    