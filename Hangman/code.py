import words
import random


def get_word():
    word = random.choice(words.word_list)
    print(word)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guesses_words = []
    tries = 6
    print("Let's play hangman")
    print(display_hangman(tries))
    print(word_completion + "\n")
    while not guessed and tries > 0:
        guess = input(f"plz guess a word or letter (remaining tries are {tries}) :").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter :)")
            elif guess not in word:
                print(guess, "is not in word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is the word!")
                guessed_letters.append(guess)
                words_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if guess == letter]
                for i in indices:
                    words_list[i] = guess
                word_completion = "".join(words_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guesses_words:
                print("you already guessed the word ", guess)
            elif guess != word:
                print("Guess is not int the word")
                tries -= 1
                guesses_words.append(guess)
            else:
                guessed = True
                word_completion = guess
        else:
            print("not a valid guess")

        print(display_hangman(tries))
        print(word_completion + "\n")

    if guessed:
        print("Congrats you guessed the word,YOU WIN :)")
    else:
        print("Sorry u ran out of tries,the word was " + word + " may be next time")


# here in list '\' is escape sequence
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play again (Y/N)").upper() == 'Y':
        word = get_word()
        play(word)


# this is code fragment so that our program will run by running  our script(code.py)  on cmd line;
if __name__ == "__main__":
    main()

# happy coding  :)
