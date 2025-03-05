import random

words = ['erendipity', 'ephemeral', 'luminous', 'quixotic',  'labyrinth', 'ethereal', 'solitude', 'melancholy', 'resilience']
art = { 0: ('     ',
            '     ',
            '     '),
        1: ('   O  ',
            '     ',
            '     '),
        2: ('   O  ',
            '   |  ',
            '     '),
        3: ('   O  ',
            '  /|  ',
            '     '),
        4: ('   O  ',
            '  /|\\',
            '     '),
        5: ('   O  ',
            '  /|\\  ',
            '  /  '),
        6: ('   O  ',
            '  /|\\  ',
            '  / \\  ')
        }

def display_man(wrong_answer):
    print('*' * 10)

    for line in art[wrong_answer]:
        print(line)
    print('*' * 10)

def display_hint(hint):
    print(' '.join(hint))

def display_answer(answer):
    print(answer)

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_answer = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_answer)
        display_hint(hint)
        guess = input('enter ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Enter a Letter')
            continue

        if guess in guessed_letters:
            print(f'{guess} is already guessed')
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_answer += 1

        if '_' not in hint:
            display_man(wrong_answer)
            display_answer(answer)
            print('You win')
            is_running = False

        elif wrong_answer == 6:
            display_man(wrong_answer)
            display_answer(answer)
            print('You lost')
            is_running = False

if __name__ == "__main__":
    main()
