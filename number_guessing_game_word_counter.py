
import random
from collections import Counter
from pathlib import Path


def number_guessing_game():
    print("\n=== Number Guessing Game ===")
    print("Guess a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Enter your guess (or q to quit): ").strip()

        if user_input.lower() == "q":
            print(f"The correct number was {secret_number}.")
            return

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            score = max(0, 100 - (attempts - 1) * 10)
            print(f"Correct! Attempts: {attempts}")
            print(f"Your score: {score}/100")
            break


def word_counter():
    print("\n=== Text File Word Counter ===")
    filename = input(
        "Enter text filename (press Enter for sample.txt): "
    ).strip()

    if not filename:
        filename = "sample.txt"
        sample_path = Path(filename)

        if not sample_path.exists():
            sample_path.write_text(
                "Python is easy. Python is useful. "
                "Practice Python every day.",
                encoding="utf-8"
            )

    try:
        text = Path(filename).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Unable to read file: {error}")
        return

    words = [
        word.strip(".,!?;:'\"()[]{}<>").lower()
        for word in text.split()
    ]
    words = [word for word in words if word]

    print(f"\nTotal words: {len(words)}")
    print(f"Unique words: {len(set(words))}")

    frequency = Counter(words)

    print("\nTop 10 most frequent words:")
    for word, count in frequency.most_common(10):
        print(f"{word}: {count}")


def main():
    while True:
        print("\n==============================")
        print(" Number Guessing & Word Counter")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Text File Word Counter")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
