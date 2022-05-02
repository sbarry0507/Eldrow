# ELDROW
from display_letters import *
import random


def main():
    c = open('eldrow_words.txt')
    total_guesses = 1
    secret = random.choice(list(open('eldrow_words.txt')))
    secret = secret.rstrip()
    correct = []
    not_in_word = []
    out_of_place = []
    summary = []
    guess = ""
    evaluate = ''
    print('WELCOME TO ELDROW!')
    print('')
    while total_guesses <= 6:
        guess = input(f'Enter guess #{total_guesses}: ')
        guess = check_in_list(guess)
        if guess == secret:  # check to see if they won
            break
        total_guesses += 1
        evaluate = evaluate_guess(guess, secret)

        banner_print(guess, evaluate)
        print('\n')

        print(evaluate_guess(guess, secret))
        summary.append(evaluate_guess(guess, secret))
        letters_used(guess, secret, not_in_word, correct, out_of_place)
        print('\nSummary:')
        print(*summary, sep='\n')
        print('\n')
    correct_fail(total_guesses)


def correct_fail(total_guesses):
    if total_guesses > 6:
        print('\n You Lose, Out of tries!')
    elif total_guesses == 1:
        print('\nCongratulations you guessed correctly, You Win! It only took',
              total_guesses, 'guess!')
    else:
        print('\nCongratulations you guessed correctly, You Win! It only took',
              total_guesses, 'guesses!')


def check_in_list(guess):
    total_guesses = 1
    c = open('eldrow_words.txt')
    txt = c.read()
    while guess not in txt:  # checking to make sure guess is in txt file
        guess = input('Invalid input. Try again:')
    return guess


def evaluate_guess(guess, secret):
    loop_continue = True
    eval_string = ''
    let_pos = 0
    while loop_continue:
        for letter in guess:

            if letter not in secret:
                eval_string += 'x'
            else:
                if guess[let_pos] == secret[let_pos]:
                    eval_string += '$'

                else:
                    eval_string += '>'

            let_pos += 1

        return eval_string


def letters_used(guess, secret, not_in_word, correct, out_of_place):
    let_pos = 0
    for i in guess:

        if i not in secret:
            not_in_word.append(i)
        else:
            if guess[let_pos] == secret[let_pos]:
                correct.append(i)

            else:
                out_of_place.append(i)
        let_pos += 1

    not_in_word = list(set(not_in_word))
    out_of_place = list(set(out_of_place))
    correct = list(set(correct))

    for i in range(len(correct)):
        correct[i] = correct[i].upper()
    for i in range(len(not_in_word)):
        not_in_word[i] = not_in_word[i].upper()
    for i in range(len(out_of_place)):
        out_of_place[i] = out_of_place[i].upper()

    print('Correct - ', end=' ')
    print(*correct)
    print('Not in word - ', end=' ')
    print(*not_in_word)
    print('Out of place - ', end=' ')
    print(*out_of_place)


if __name__ == "__main__":
    main()
