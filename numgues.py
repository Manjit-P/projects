import random

lowest_value = 1
highest_value = 100
is_running = True
computer_choice = random.randint(lowest_value,highest_value)

print('Number Guessing Game')
print("*" * 30)

player_choice = (input(f'Guess a number {lowest_value}-{highest_value} '))
guess = 0

while is_running == True:

    if not player_choice.isdigit():
        player_choice = (input(f'Guess a number {lowest_value}-{highest_value} '))
        is_running == True
    else:
        guess += 1
        player_choice = int(player_choice)
        if player_choice < lowest_value or player_choice > highest_value:
            player_choice = (input(f'Guess a number {lowest_value}-{highest_value} '))
            is_running == True  
        elif (player_choice) > (computer_choice):
            player_choice = (input('Go Lower '))
            is_running = True
        elif (player_choice) < (computer_choice):
            player_choice = (input('Go Higher '))
            is_running = True
        else:
            print(f"You guessed it right in {guess} guesses. OMEDETOU 👏")
            is_running = False