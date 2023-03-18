# user is gone guess the number
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x} :"))
        if guess>random_number:
            print("its too high")
        elif guess<random_number:
            print("its too low")

    print(f"Yay.congrats,you guessed the number {guess}")


guess(10)




