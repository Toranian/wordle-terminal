import sys, os
from turtle import clear
from colorama import init
from termcolor import colored
from random import choice
from time import sleep
init()



cant_use = []
print("Welcome to Wordle!")
def load_words(filename: str) -> list:

	full_path = os.getcwd() + "/" + filename
	with open(full_path, 'r') as f:
		return [line.strip() for line in f]

def pick_word(words: list) -> str:
	return choice(words)

def calc_word(word, goal_word):
	for letter_index in range(len(word)):
		letter = word[letter_index]

		if letter in goal_word and letter==goal_word[letter_index]:
			print("["+ colored(letter, 'green', attrs=["bold"])+"]", end='')
		elif letter in goal_word:
			print("[" + colored(letter, 'yellow') + "]", end='')
		else:
			print("[" + colored(letter, 'white') + "]", end='')

			if letter not in cant_use:
				cant_use.append(letter)
		sleep(0.1)
	print()


def print_words(word_bank, goal_word, attempts):
	for word in word_bank:
		calc_word(word, goal_word)
	print("[] [] [] [] []\n" * attempts)

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def main():
	all_words = load_words('words.txt')
	goal_word = pick_word(all_words)
	word_bank = []
	attempts = 6

	while attempts > 0:
		print_words(word_bank, goal_word, attempts)
		
		if len(cant_use) > 0:
			print("You can't use:", end=' ')
			for letter in cant_use:
				print(letter + ", ", end='')
			print()
		in_word = input("Enter a word: ")

		if in_word == goal_word:
			word_bank.append(in_word)
			print_words(word_bank, goal_word, attempts)
			print(f"You beat the game in only {6-attempts} attempts!")
			sys.exit(0)
		
		elif in_word == "quit" or in_word == "exit":
			print("See you next time!")
			sys.exit(0)

		elif in_word not in all_words:
			print("Sorry, that's not a word!")
		
		elif in_word in all_words:
			word_bank.append(in_word)
			attempts -= 1
		
		
		else:
			attempts -= 1
			print("You have", attempts, "attempts left.")
		
		clear_screen()
		
	print(f"\nYou lost! The word was {goal_word}")

main()
