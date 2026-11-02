import random
WORDS = ["python", "hangman", "computer", "garden", "planet"]
MAX_INCORRECT_GUESSES = 6


def play() -> None:
    word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word one letter at a time. You can make {MAX_INCORRECT_GUESSES} incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")

        if all(letter in guessed_letters for letter in word):
            print(f"You win! The word was {word}.")
            return

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess in word:
                print("Good guess!")
            else:
                incorrect_guesses += 1
                print("That letter is not in the word.")

    print(f"\nYou ran out of guesses. The word was {word}.")


if __name__ == "__main__":
    play()
