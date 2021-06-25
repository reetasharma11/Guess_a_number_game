# Guess a number between 1 and 100
import random
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
MEDIUM_LEVEL_TURN = 7


def check_answer(guess, answer, turns):
    """ Checks answer against the guess. Return the remaining number of turns """
    if guess == answer:
        print(f"You got it. It was {answer}")
    elif guess > answer:
        print("It's too high.")
        return turns - 1
    elif guess < answer:
        print("It's too low.")
        return turns - 1


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' or 'medium': ").lower()

    if level == "easy":
        return EASY_LEVEL_TURN
    elif level == "hard":
        return HARD_LEVEL_TURN
    elif level == "medium":
        return MEDIUM_LEVEL_TURN


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guess. you lose.")
            return
        elif guess != answer:
            print("guess again")


game()

