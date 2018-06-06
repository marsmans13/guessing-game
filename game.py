from random import randint

print("Hello!")
player_name = input("Enter your name: ")

lowest_score = None


while True:
    low = int(input("Enter the lower bound of your range: "))
    high = int(input("Enter the lower bound of your range: "))
    random_nums = randint(low, high)
    count = 0
    guess = 0
    while guess != random_nums and count < 6:
        guess = int(input("Enter a number between {} and {}: ".format(low, high)))
        count += 1
        if guess not in range(low, high + 1):
            print("Try again. Pick a number between {} and {}: ".format(low, high))
        elif guess > random_nums:
            print("Too high.")
        elif guess < random_nums:
            print("Too low.")

    if count == 10:
        print("Too many tries.")
    elif lowest_score is None or count < lowest_score:
        lowest_score = round((count / (high - low)) * 100)
        print("Your new low score is: {}".format(lowest_score))
    elif random_nums == guess:
        print("You guessed it in {} tries.".format(count))
    play_again = input("Would you like to play again? Y/N: ")
    if play_again.upper() == 'N':
        print("Thanks for playing!")
        break
    else:
        pass
