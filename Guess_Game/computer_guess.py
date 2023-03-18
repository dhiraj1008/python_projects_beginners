# computer is gone guess the number
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback.lower() != 'c':
        print(f"{low} {high}")
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low  # it can be even high
        feedback = input(f"is {guess} too high(h),too low(l) ,or correct(c)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay. congrats your compter gussed the number {guess} correctly :)");


computer_guess(9)
