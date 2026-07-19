import random

def choose_word():
    """Randomly select a word from a predefined list."""
    words = ["python", "hangman", "computer", "internship", "keyboard"]
    return random.choice(words)

def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    print(f"You have {max_wrong_guesses} incorrect guesses allowed.\n")

    while wrong_guesses < max_wrong_guesses:
        print("Word: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")

        if all(letter in guessed_letters for letter in word):
            print("Word: " + display_progress(word, guessed_letters))
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! You've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
