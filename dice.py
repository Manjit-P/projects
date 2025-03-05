import random

art = {
        1: ('⬜️⬜️⬜️⬜️⬜',
            '⬜️⬜️⬜️⬜️⬜️',
            '⬜️⬜️⬛️⬜️⬜️',
            '⬜️⬜️⬜️⬜️⬜️',
            '⬜️⬜️⬜️⬜️⬜️'), 

        2: ('⬜️⬜️⬜️⬜️⬜',
            '⬜️⬜️⬜️⬛️⬜️',
            '⬜️⬜️⬜️⬜️⬜️',
            '⬜️⬛️⬜️⬜️⬜️',
            '⬜️⬜️⬜️⬜️⬜️'), 

        3: ('⬜️⬜️⬜️⬜️⬜',
            '⬜️⬜️⬜️⬛️⬜️',
            '⬜️⬜️⬛️⬜️⬜️',
            '⬜️⬛️⬜️⬜️⬜️',
            '⬜️⬜️⬜️⬜️⬜️'),

        4: ('⬜️⬜️⬜️⬜️⬜',
            '⬜️⬛️⬜️⬛️⬜️',
            '⬜️⬜️⬜️⬜️⬜️',
            '⬜️⬛️⬜️⬛️⬜️',
            '⬜️⬜️⬜️⬜️⬜️'),

        5: ('⬜️⬜️⬜️⬜️⬜',
            '⬜️⬛️⬜️⬛️⬜️',
            '⬜️⬜️⬛️⬜️⬜️',
            '⬜️⬛️⬜️⬛️⬜️',
            '⬜️⬜️⬜️⬜️⬜️'),

        6: ('⬜️⬜️⬜️⬜️⬜',
            '⬜️⬛️⬛️⬛️⬜️',
            '⬜️⬜️⬜️⬜️⬜️',
            '⬜️⬛️⬛️⬛️⬜️',
            '⬜️⬜️⬜️⬜️⬜️') 
}


dice = [1, 2, 3, 4, 5, 6]
def roll(dice_number,total = 0):
    i=0
    while i != dice_number:
        value = random.choice(dice)
        total += value
        print(' ')
        for line in art[value]:
           for ie in line:
               print(ie,end='')
           print(' ')
        i += 1
    print(f'Total: {total}')
def ask():
    dice_number = input('Enter the number of times you want to roll ')
    roll(int(dice_number))    
ask() 