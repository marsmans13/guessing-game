from random import randint

print("Hello! Guess a number between 1 and 100!")
player_name = input("Enter your name: ")


def guessing_game():
    random_nums = randint(1, 100)
    count = 0
    guess = 0

    while guess != random_nums:
        guess = int(input("Enter a number between 1 and 100: "))
        if guess not in range(1, 101):
            print("Try again. Pick a number between 1 and 100: ")

        elif guess > random_nums:
            print("Too high.")
            count += 1
        elif guess < random_nums:
            print("Too low.")
            count += 1
    print("You guessed it in {} tries.".format(count))
    play_again = input("Would you like to play again? Y/N: ")
    if play_again.upper() == 'N':
        print("Thanks for playing!")
    else:
        guessing_game()


guessing_game()
