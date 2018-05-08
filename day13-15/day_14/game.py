import random
from collections import namedtuple
from Selection import Selection, Rock, Sissor, Paper, player


def main():
    print_header()
    user = game_user()
    main_player = player(user)
    Computer = player("PC")
    rolls = define_rolls()
    game_loop(main_player, Computer, rolls)


def print_header():
    print('---------------------------------')
    print('          ROCK, PAPER, SCISSORS')
    print('---------------------------------')
    print()


def game_user():
    user = input("Enter your name: ")
    return user

def define_rolls():
    rolls = namedtuple('roll', 'rock paper sissor')
    return rolls(Rock('Rock'), Paper('Paper'), Sissor('Sissor'))

def game_loop(user, computer, rolls):

    count = 0
    while count < 3:
        PC_Choice = random.choice(rolls)
        print('PC player is ready')
        cmd = input('Your decision is [r]ock, [s]issor, or [p]aper? ')
        if cmd == 'r':
            User_Choice = Rock('Rock')
        elif cmd == 's':
            User_Choice = Sissor('Sissor')
        elif cmd == 'p':
            User_Choice = Paper('Paper')
        if User_Choice.vs(PC_Choice):
            user.score+=1
        else:
            computer.score+=1
        print('Your choice is {}, Computer\'s choice is {}\n'.format(User_Choice.name, PC_Choice.name))
        count+=1

    if computer.score>user.score:

        print('{} is the winner'.format(computer.name))
    else:
        print('{} is the winner'.format(user.name))
    print('Score board: {}: {}\t\t{}: {}'.format(user.name, user.score, computer.name, computer.score))

if __name__ == '__main__':
    main()
