#rockpaperscissors

import random

while True:
    user = input('What is your choice? (rock, paper, scissors):\n')
    user = user.lower()
    action_list = ['rock','paper','scissors']
    computer = random.choice(action_list)

    print(f"You choose {user}, computer chooses {computer}")

    if user == computer:
        print("It's a tie!")
    elif user == 'rock':
        if computer == 'scissors':
            print('You win!')
        else:
            print('You lose!')
    elif user == 'paper':
        if computer == 'rock':
            print('You win!')
        else:
            print('You lose!')
    elif user == 'scissors':
        if computer == 'rock':
            print('You lose!')
        else:
            print('You win!')
    
    again = input('Would you like to retry? (Y/N):\n')
    if again.upper() =='Y':
        continue
    else:
        break




