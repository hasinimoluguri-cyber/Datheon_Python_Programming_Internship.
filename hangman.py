import random

# Words used in the game
WORDS = ["PYTHON", "COMPUTER", "PROGRAM", "DEVELOPER", "KEYBOARD", "SCIENCE"]

# Hangman drawings: one stage for each number of wrong guesses
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def display_word(secret_word, guessed_letters):
    """Show guessed letters and hide the letters not guessed yet."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("=" * 35)
    print("       HANGMAN WORD GUESSING GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {max_attempts} incorrect guesses available.")

    while wrong_guesses < max_attempts:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
        print(f"Attempts left: {max_attempts - wrong_guesses}")

        guess = input("Enter one letter: ").strip().upper()

        # Validate the user's input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.\n")
            continue

        # Repeated letters do not reduce attempts
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!\n")
            if all(letter in guessed_letters for letter in secret_word):
                print("Word:", secret_word)
                print("Congratulations! You guessed the word.")
                return
        else:
            wrong_guesses += 1
            print("Incorrect guess!\n")

    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Game over! The correct word was: {secret_word}")


if __name__ == "__main__":
    play_game()
