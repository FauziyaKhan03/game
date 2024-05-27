import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    name = input("May I ask you for your name? ")
    print(f"Hello, {name}! I have chosen a number between 1 and 200. Try to guess it!")

    secret_number = random.randint(1, 200)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations, {name}! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

def main():
    while True:
        guessing_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

