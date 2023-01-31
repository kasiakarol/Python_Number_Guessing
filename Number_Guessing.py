from random import randint
from Logo import logo
from Clear_function import clear


def play_again():
    if_play_again = input("Would you like to play again? Y/N: ")
    if if_play_again.upper() == "Y":
        clear()
        return True


print(logo)
while True:
    try:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        guess_count = 0
        if level.lower() == 'easy':
            guess_count = 10
        elif level.lower() == 'hard':
            guess_count = 5
        else:
            print("Incorrect input")
            continue

        random_number = randint(1, 100)

        while guess_count >= 1:
            # print("Random number is", random_number)
            print("Number of your guesses is", guess_count)
            guess = int(input("Make a guess: "))
            guess_count = guess_count - 1
            print("Your guess is", guess)

            if guess == random_number:
                print(f"You got it! The answer was {guess}")
                break
            elif guess > random_number:
                print("Too high!")
            elif guess < random_number:
                print("Too low!")

        else:
            print("No guesses available. Game over.\n")

    except ValueError:
        print("Incorrect input. Game over")

    if not play_again():
        break
