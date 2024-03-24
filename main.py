import random

easy_count = 10
hard_count = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too High')
        return turns - 1
    elif guess < answer:
        print('Too Low ')
        return turns - 1
    else:
        print(f'You got it right. The answer was {answer}')


def set_difficulty():
    level = input('Chose a difficulty: Type "easy" or "hard" : ')
    if level == 'easy':
        return easy_count
    elif level == 'hard':
        return hard_count


def game():
    print('Welcome To Guess The Number Game ! ')
    print('I am thinking of a number between 1 to 100 ..')

    number = random.randint(1, 100)

    turns = set_difficulty()

    user_input = 0
    while user_input != number:
        print(f'You have {turns} attempts left to guess the number')

        user_input = int(input('Make a Guess : '))

        turns = check_answer(user_input, number, turns)
        if turns == 0:
            print('You run out of moves. you Lose')
            break


game()
