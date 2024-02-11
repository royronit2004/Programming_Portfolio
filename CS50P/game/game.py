# guessing game

import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break

    except:
        pass

rand_num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess > rand_num:
            print("Too large!")
        elif guess < rand_num:
            print("Too small!")
        else:
            print("Just right!")
            break

    except:
        pass
