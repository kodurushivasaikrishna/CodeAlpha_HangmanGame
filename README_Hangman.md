🪓 Hangman Game — CodeAlpha Task 1

A classic text-based Hangman game built entirely in Python as part of the CodeAlpha Python Programming Internship.
---
📌 About the Project

The player must guess a hidden word one letter at a time. Each wrong guess brings the hangman one step closer to completion. The game ends when the player either guesses the full word or runs out of attempts.
---
🎮 How to Play

Run the game in your terminal.
A word is chosen at random — you'll see blanks representing each letter.
Type one letter at a time and press Enter.
You have 6 wrong guesses before the hangman is complete and you lose.
Guess all the letters correctly to win!
---
✨ Features

🎲 Random word selection from a built-in word list
🖼️ ASCII art hangman that updates after each wrong guess
✅ Tracks correct and incorrect guesses
⚠️ Validates input — prevents duplicate guesses and non-letter entries
🔁 Option to replay after each game
---
🛠️ Concepts Used

Concept	Usage
`random` module	Randomly selects a word
`while` loop	Keeps the game running
`if-else` statements	Handles correct/incorrect guesses
Sets & Strings	Tracks guessed letters and word progress
Functions	Organized, reusable code structure
---
🚀 How to Run

Make sure Python 3 is installed on your system.
```bash
# Clone the repository
git clone https://github.com/YourUsername/CodeAlpha\_HangmanGame.git

# Navigate to the folder
cd CodeAlpha\_HangmanGame

# Run the game
python hangman.py
```
---
📸 Sample Output

```
========================================
   Welcome to HANGMAN!
========================================
The word has 6 letters. You have 6 wrong guesses allowed.

       -----
       |   |
           |
           |
           |
           |
    =========

Word:  \_ \_ \_ \_ \_ \_
Guessed letters: None
Wrong guesses left: 6

Guess a letter: p
✅  Nice! 'p' is in the word.
```
---
👤 Author
[Your Name]
CodeAlpha Python Programming Internship
---
🏢 Internship
This project was built as Task 1 of the CodeAlpha Python Programming Internship.
🔗 CodeAlpha Website
