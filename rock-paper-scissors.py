from random import choice

while True:
    computer_choice = choice(['rock', 'paper', 'scissors'])
    user_choice = input('Your turn, please choose rock, paper or scissors\n')
    if user_choice == 'exit': break

    print(f'Computer choice is {computer_choice}')

    if computer_choice == user_choice:
        print('TIE')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('YOU WIN')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('YOU WIN')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('YOU WIN')
    else:
        print('You lose :( Computer wins :D')