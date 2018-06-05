from random import randint

print("Hello! Guess a number between 1 and 100!")
player_name = input("Enter your name: ")
random_nums = randint(1, 100)
count = []
guess = 0

while guess != random_nums:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess not in range(1, 101):
        print("Try again. Pick a number between 1 and 100: ")

    elif guess > random_nums:
        print("Too high.")
        count.append(guess)
    else:
        print("Too low.")
        count.append(guess)
print("You guessed it in {} tries.".format(len(count)))
