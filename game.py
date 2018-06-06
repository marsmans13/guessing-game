from random import randint

print("Hello! Guess a number between 1 and 100!")
player_name = input("Enter your name: ")

lowest_score = None


while True:
    random_nums = randint(1, 100)
    count = 0
    guess = 0
    while guess != random_nums:
        guess = int(input("Enter a number between 1 and 100: "))
        count += 1
        if guess not in range(1, 101):
            print("Try again. Pick a number between 1 and 100: ")
        elif guess > random_nums:
            print("Too high.")
        elif guess < random_nums:
            print("Too low.")
    print("You guessed it in {} tries.".format(count))
    # if count < lowest_score or lowest_score is None:
    if lowest_score is None or count < lowest_score:
        print("Your new low score is: {}".format(count))
        lowest_score = count
    play_again = input("Would you like to play again? Y/N: ")
    if play_again.upper() == 'N':
        print("Thanks for playing!")
        break
    else:
        pass
