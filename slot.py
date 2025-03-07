import random

def payout(result,bet):
    if result[0]==result[1]==result[2]:
        print(f'YOU WON ${bet*10}')

        return bet * 10
    else:
        print(f'YOU LOST ${bet}')

        return bet

def spin():
    slot_art = ['🍒','🍌','🍎','🍍','🍇']
    return list((random.choice(slot_art) for _ in range(5)))

def main():
    balance = 100
    print('*' * 20)
    print('SLOT MACHINE')
    print('🍒 🍌 🍎 🍍 🍇')
    print(' ')
    print('*' * 20)
    print('*' * 20)
    print(f'YOUR BALANCE: ${balance}')

    while balance > 0:
        result = []
        bet = input('ENTER YOUR BET: $')
        if not bet.isdigit():
            print('INVALID INPUT')
            continue
        bet = int(bet)
        if bet > balance:
            print('INSUFFICIENT FUNDS')
            continue
        if bet <= 0:
            print('BET MUST BE GREATER THAN $0')
            continue

        result =spin()
        print(' |'.join(result))
        pay = payout(result,bet)
        if pay > bet:
            balance += pay
            print(f'YOUR BALANCE: ${balance}')
        else:
            balance -= bet
            print(f'YOUR BALANCE: ${balance}')
        if balance == 0:
            print("You lost. ")
            break
        play_again = input("DO YOU WANT TO SPIN AGAIN (y/n)? ").lower()
        if play_again != 'y':
            print('*'*20)
            print('*'*20)
            print(f'FINAL BALANCE: ${balance}')
            break
        if play_again == 'y':
            continue


if __name__ == '__main__':
    main()