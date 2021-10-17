#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

EASY_LEVEL, HARD_LEVEL = 5, 10


def welcome_user():
    print(logo)

    start_game_text = [
        f'Welcome to the Number Guessing Game!',
        'I\'m thinking of a number between 1 and 100.',
        'Pssst, the correct answer is {} ... syke!'.format(randint(2, 99)),
    ]

    print(start_game_text[0])
    print(start_game_text[1])
    print(start_game_text[2])


def get_user_input(state):
    if state == 'start':
        return input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    elif state == 'in game':
        return int(input('Make a guess: '))


def select_game_difficulty(user_input):
    return HARD_LEVEL if user_input == 'easy' else EASY_LEVEL


def get_correct_number():
    return randint(2, 99)


def compare_user_guess(guess_attempts, user_input, the_correct_number):
    while (guess_attempts > 0) and (user_input != the_correct_number):
        print(f'You have {guess_attempts} attempts remaining to guess the number.')

        user_input = int(input('Make a guess: '))

        print(give_user_hint(user_input, the_correct_number))

        guess_attempts -= 1
    else:
        print(track_user_progress(user_input, the_correct_number))


def give_user_hint(user_input, the_correct_number):
    if user_input > the_correct_number:
        print('Too high.')
    elif user_input < the_correct_number:
        print('Too low.')
    
    return 'Guess again.'


def track_user_progress(user_input, the_correct_number):
    if user_input != the_correct_number:
        return 'You\'ve run out of guesses, you lose.'
    else:
        return f'You got it! The answer was {the_correct_number}.'


def play_guessing_game():
    welcome_user()
    user_input = get_user_input('start')
    guess_attempts = select_game_difficulty(user_input)
    the_correct_number = get_correct_number()
    compare_user_guess(guess_attempts, user_input, the_correct_number)


play_guessing_game()