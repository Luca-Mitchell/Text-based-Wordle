import random

yellow = "\033[0;33m"
green = "\033[0;32m"
reset = "\033[0m"

def pick_word(file_path):
    with open(file_path, "r") as file:
        words = [line.strip().upper() for line in file.readlines()]
        return random.choice(words)
    
def check_guess(actual_word, guess):
    num_correct = 0
    guessed_letters = []
    for index, letter in enumerate(guess):
        if letter == actual_word[index]:
            guessed_letters.append(f"{green}{letter}{reset}")
            num_correct += 1
        elif letter in actual_word:
            guessed_letters.append(f"{yellow}{letter}{reset}")
        else:
            guessed_letters.append(letter)
    return " ".join(guessed_letters), num_correct

def valid_guess(guess, file_path):
    with open(file_path, "r") as file:
        words = [line.strip().upper() for line in file.readlines()]
        return guess in words

def run_game():
    word = pick_word("words.txt")
    msg = ""
    game_over = False
    counter = 1
    while game_over == False:
        print(f"GUESS: {counter}")
        guess = input("guess: ").upper()
        if valid_guess(guess, "words.txt"):
            checked_guess, num_correct = check_guess(word, guess)
            print(checked_guess)
            if counter == 6:
                game_over = True
                msg = f"The word was {word}"
            elif num_correct == 5:
                game_over = True
                msg = "Correct!"
            counter += 1
        else:
            print("Not in word list")
        print("-----------------------------------------------")
    print(msg)

if __name__ == "__main__":
    run_game()
