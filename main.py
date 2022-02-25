import sys
import os
from colorama import init
from termcolor import colored
from random import choice
from time import sleep
init()

# Global variables
cant_use = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
correct_letters = []

# Load the words from the wordlist file


def load_words(filename: str) -> list:

    full_path = os.getcwd() + "/" + filename
    with open(full_path, 'r') as f:
        return [line.strip() for line in f]

# Pick a random word


def pick_word(words: list) -> str:
    return choice(words)

# Display the word with colored letters


def calc_word(word, goal_word):
    for letter_index in range(len(word)):
        letter = word[letter_index]

        if letter in goal_word and letter == goal_word[letter_index]:
            print("[" + colored(letter, 'green', attrs=["bold"])+"]", end='')
        elif letter in goal_word:
            print("[" + colored(letter, 'yellow') + "]", end='')
        else:
            print("[" + colored(letter, 'white', attrs=['bold']) + "]", end='')

            if letter not in cant_use:
                cant_use.append(letter)
            else:
                correct_letters.append(letter)
    print()


# Print out the letters that can't be used, and the ones that can
def print_letters(cant_use, letters):
    for letter in letters:
        if letter == "m":
            print()
        elif letter in cant_use:
            print(colored(letter, 'red') + " ", end='')
        else:
            print(colored(letter, 'white') + " ", end='')
    print()


# Print out the words in the word bank
def print_words(word_bank, goal_word, attempts):
    for word in word_bank:
        calc_word(word, goal_word)
    print("[ ][ ][ ][ ][ ]\n" * attempts)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    all_words = load_words('words.txt')
    goal_word = pick_word(all_words)
    word_bank = []
    attempts = 6
    status = ""

    while attempts > 0:

        if len(status) > 0:
            print(status)
            status = ""

        print_words(word_bank, goal_word, attempts)

        if len(cant_use) > 0:
            print_letters(cant_use, alphabet)

        in_word = input("\nEnter a word: ")

        if in_word == goal_word:
            word_bank.append(in_word)
            print_words(word_bank, goal_word, attempts)
            print(f"You beat the game in only {6-attempts} attempts!")
            sys.exit(0)

        elif in_word == "quit" or in_word == "exit":
            print("See you next time!")
            sys.exit(0)

        elif in_word == "hint":
            for letter in goal_word:
                if letter not in correct_letters:
                    print("Hint: " + colored(letter, 'yellow'))
                    sleep(2)

        elif in_word not in all_words:
            status = "Sorry, that's not a word!\n"

        elif in_word in all_words:
            word_bank.append(in_word)
            attempts -= 1

        else:
            attempts -= 1
            print("You have", attempts, "attempts left.")

        clear_screen()

    print_words(word_bank, goal_word, attempts)
    print(f"\nYou lost! The word was {goal_word}")


main()
