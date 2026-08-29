"""
Hangman Game
============
A classic text-based Hangman game built in Python.
Player guesses a hidden word one letter at a time with 6 allowed mistakes.

Author: [Your Name]
Internship: CodeAlpha Python Programming Internship
Task: Task 1 - Hangman Game
"""

import random

# ─────────────────────────────────────────────
#  Word list
# ─────────────────────────────────────────────
WORD_LIST = ["python", "hangman", "developer", "keyboard", "monitor"]

# ─────────────────────────────────────────────
#  Hangman ASCII art stages (0 = fresh, 6 = dead)
# ─────────────────────────────────────────────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]


def choose_word():
    """Pick a random word from the word list."""
    return random.choice(WORD_LIST)


def display_board(stage, word_letters, guessed_letters):
    """Print the hangman figure, word progress, and guessed letters."""
    print(HANGMAN_STAGES[stage])
    print("Word: ", " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word_letters
    ))
    print(f"\nGuessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")


def get_valid_guess(guessed_letters):
    """Ask the player for a single alphabetic letter they haven't tried yet."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❌  Please enter a single letter (a–z).")
        elif guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman():
    """Run one full game of Hangman."""
    word = choose_word()
    word_letters = set(word)   # unique letters in the word
    guessed_letters = set()    # letters the player has guessed
    wrong_guesses = 0
    max_wrong = 6

    print("\n" + "=" * 40)
    print("   Welcome to HANGMAN!")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have {max_wrong} wrong guesses allowed.\n")

    # ── Main game loop ──
    while wrong_guesses < max_wrong and word_letters - guessed_letters:
        display_board(wrong_guesses, word, guessed_letters)
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word_letters:
            print(f"✅  Nice! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌  '{guess}' is not in the word. -{1} life.")

    # ── End-of-game message ──
    print("\n" + "=" * 40)
    if word_letters <= guessed_letters:
        print(f"🎉  You WON! The word was: {word.upper()}")
    else:
        display_board(wrong_guesses, word, guessed_letters)
        print(f"💀  You LOST! The word was: {word.upper()}")
    print("=" * 40)


def main():
    """Entry point – allows replaying."""
    while True:
        play_hangman()
        again = input("\nPlay again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye. 👋")
            break


if __name__ == "__main__":
    main()
