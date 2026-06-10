
# 📘 Assignment: 🎮 Hangman Game

## 🎯 Objective

Build a command-line Hangman (Ahorcado) game in Python that exercises string manipulation, loops, conditionals, and user input handling.

## 🧾 Background

This project recreates the classic word-guessing Hangman game. Students will implement game logic, display progress, and handle win/lose conditions.

## 🧰 Starter Code

Use the provided starter file: `starter-code.py` (located in the same folder). Run the program with:

```bash
python3 starter-code.py
```

If you prefer, copy the starter code into a new file named `hangman.py` and submit that file when complete.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Complete the starter code so the program runs a playable Hangman game in the terminal.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list (or from `data/words.txt` if provided).
- Accept single-letter guesses (case-insensitive) and update the revealed letters accordingly.
- Display the current word progress using underscores for unknown letters (for example: `_ a _ _ m a n`).
- Track and display remaining attempts; decrement on incorrect guesses.
- Prevent repeated guesses from counting against the player and inform the player if a letter was already guessed.
- End the game with a clear win or lose message and reveal the secret word on loss.
- Include at least basic input validation (reject empty input or multi-character guesses).

## 🧪 Examples

Example interaction (user input shown after `>`):

```text
Welcome to Hangman!
Word: _ _ _ _ _
Guesses left: 6
Guess a letter: > a
Good guess!
Word: _ a _ _ _
Guesses left: 6
```

## 📤 Submission

- Submit a single Python file named `hangman.py` in the assignment folder, or update `starter-code.py` and create a PR with your changes.
- Include brief usage notes in the PR description (how to run the game).

## ⏱️ Estimated Time

45–60 minutes

## ⚖️ Difficulty

Beginner

## 🧾 Grading Notes (for TAs)

- Verify correct random word selection and accurate progress display.
- Check input validation and duplicate-guess handling.
- Confirm clear win/lose messages and that the secret word is revealed on loss.

---

**Files in this assignment folder**: `starter-code.py` (starter code). Verify any additional data files are linked with relative paths.

If you want, I can convert other assignments to this template as well.
