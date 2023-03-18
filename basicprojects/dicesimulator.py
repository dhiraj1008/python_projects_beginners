#import random
#define roll_dice function
#createto  dictionary to store the values of dice and their corresponding images.!

import random

def roll_dice():

    choice = input("Roll the dice (yes/no)\n")
    while choice.lower() == 'yes':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)

        print("dice rolled : {} and {}".format(dice1,dice2))
        print(simulator(dice1))
        print(simulator(dice2))

        choice = input("Roll the dice (yes/no)\n")

def simulator(value):
        #dict to store images and values of the dice
    dict_vi ={
    1:
       (   "  __________ ",
           " |          |",
           " |   (1)    |",
           " |    *     |",
           " |__________|"
       ),
    2:
       (    "  __________ ",
            " |          |",
            " |   (2)    |",
            " | *      * |",
            " |__________|"
       ),
    3: 
       (    " __________ ",
            "| *        |",
            "|    *     |",
            "|   (3)  * |",
            "|__________|"
        ),
    4: 
       (   "  __________ ",
           " |  *     * |",
           " |          |",
           " |  * (4) * |",
           " |__________|"
        ),
    5: 
       (    " __________ ",
            "| *      * |",
            "|     *    |",
            "| *  (5) * |",
            "|__________|"
        ),
    6: 
       (   " __________ ",
           "| *      * |",
           "| *      * |",
           "| * (6)  * |",
           "|__________|",
       ),    
    }
    return "\n".join(dict_vi[value])


roll_dice()