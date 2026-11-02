# Hangman (Python)

A simple command-line Hangman game written in Python. The computer picks a random word, and you guess it one letter at a time before you run out of incorrect guesses.

Built as a beginner-friendly project (CodeAlpha Python programming task).

## Features

- Random word chosen from a built-in word list
- 6 incorrect guesses allowed (configurable)
- Input validation: only a single alphabetic letter is accepted
- Detects repeated guesses without penalizing you
- Case-insensitive input
- Clear win/lose messages that reveal the word
- No external dependencies (uses only the Python standard library)

## Requirements

- Python 3.6 or newer (uses f-strings and type hints)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. Run the game:

   ```bash
   python CODEALPHA.py
   ```

   On some systems use `python3` instead of `python`.

## How to Play

1. The game shows the word as underscores, one per letter, for example `_ _ _ _ _ _`.
2. Type a single letter and press Enter.
3. A correct letter is revealed in every position where it appears.
4. A wrong letter adds one to your incorrect-guess count.
5. You win by revealing the whole word. You lose after 6 incorrect guesses.

### Example Session

```
Welcome to Hangman!
Guess the word one letter at a time. You can make 6 incorrect guesses.

Word: _ _ _ _ _ _
Incorrect guesses: 0/6
Guess a letter: p
Good guess!

Word: p _ _ _ _ _
Incorrect guesses: 0/6
Guess a letter: z
That letter is not in the word.
...
You win! The word was python.
```

## Configuration

Edit the constants at the top of `CODEALPHA.py`:

```python
WORDS = ["python", "hangman", "computer", "garden", "planet"]
MAX_INCORRECT_GUESSES = 6
```

- `WORDS`: add or remove words to change what can be chosen.
- `MAX_INCORRECT_GUESSES`: make the game easier or harder.

## How It Works

- `random.choice(WORDS)` selects the secret word.
- `guessed_letters` stores every letter the player has tried.
- Each turn the word is displayed with unguessed letters hidden as `_`.
- The loop ends when all letters are guessed (win) or `incorrect_guesses` reaches the maximum (lose).

## Project Structure

```
.
├── CODEALPHA.py   # Game source code
└── README.md
```

## Ideas for Improvement

- ASCII-art hangman drawing that updates with each wrong guess
- Show the list of letters already guessed
- Load words from a file or add difficulty levels / categories
- "Play again?" option after each game
- Unit tests for the guess-handling logic

## Contributing

Suggestions and pull requests are welcome. Feel free to open an issue.

## License

Add a license of your choice (for example MIT).
