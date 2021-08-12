from art import logo
from random import randint

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def set_difficulty():
	"""Asks user for difficulty and sets lives counter"""
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty == 'hard':
		return EASY_LEVEL_LIVES
	elif difficulty == 'easy':
		return HARD_LEVEL_LIVES

def check_answer(guess, answer, lives):
	"""Checks if answer is correct"""
	if guess > answer:
		print("Too high\nGuess again")
		return lives - 1
	elif guess < answer:
		print("Too low\nGuess again")
		return lives - 1
	else:
		print(f"You got it! The answer was {answer}")

def play_game():
	"""Starts game"""
	print(logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100")
	answer = randint(1, 100)
	lives = set_difficulty()
	guess = 0
	while guess != answer:
		guess = int(input("Make a guess: "))
		lives = check_answer(guess, answer, lives)



if __name__ == "__main__":
	play_game()	
