import random
import csv
import sys
from collections import namedtuple

import logbook
from Support import Roll, Player

api_log = logbook.Logger('Game_log')

def main():
    print_header()
    maindict = read_rolls()
    #print(maindict)
    user = game_user()
    main_player=Player(user)
    computer=Player('computer')
    rolls = create_rolls()
    game_loop(main_player,computer,rolls, maindict)

def print_header():
    print('---------------------------------')
    print('          Unknown Game')
    print('---------------------------------')
    print()

def read_rolls():
    maindict={}
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            row_name = row['Attacker']
            sub_row = read_roll(row)
            new_dict = {row_name.lower() : sub_row}
            maindict.update(new_dict)
    return maindict

def read_roll(row: dict):
    del row['Attacker']
    sub_row=[]
    for k in row.keys():
        can_defeat = row[k].strip().lower()
        if can_defeat == 'win':
            sub_row.append(k.lower())
    return sub_row


def create_rolls():
    rolls = namedtuple('roll', 'rock gun lightning devil dragon water air paper sponge wolf tree human snake scissors fire')
    return rolls(Roll('rock'),Roll('gun'),Roll('lightning'),Roll('devil'),Roll('dragon'),
                 Roll('water'),Roll('lair'),Roll('paper'),Roll('sponge'),Roll('wolf'),
                 Roll('tree'),Roll('human'),Roll('snake'),Roll('scissors'),Roll('fire'))


def game_user():
    user = input("Enter your name: ")
    return user


def game_loop(player, computer, rolls, dict):
    count = 0
    print('PC player is ready')
    string = ("Select from [r]ock, [g]un, [l]ightning, [d1]evil, [d2]ragon, [w]ater, \n"
          "[a]ir, [p]aper, [s]ponge [w]olf, [t]ree, [h]uman, [s1]snake, [s2]cissors or [f]ire\n")
    print(string)
    while count < 3:
        PC_choice = random.choice(rolls)
        cmd = input('Your decision is: ')

        print()

        if cmd == 'r':
            User_choice = Roll('rock')
        elif cmd == 'g':
            User_choice = Roll('gun')
        elif cmd == 'l':
            User_choice = Roll('lightning')
        elif cmd == 'd1':
            User_choice = Roll('devil')
        elif cmd == 'd2':
            User_choice = Roll('dragon')
        elif cmd == 'w':
            User_choice = Roll('water')
        elif cmd == 'a':
            User_choice = Roll('air')
        elif cmd == 'p':
            User_choice = Roll('paper')
        elif cmd == 's':
            User_choice = Roll('sponge')
        elif cmd == 'w':
            User_choice = Roll('wolf')
        elif cmd == 't':
            User_choice = Roll('tree')
        elif cmd == 'h':
            User_choice = Roll('human')
        elif cmd == 's1':
            User_choice = Roll('snake')
        elif cmd == 's2':
            User_choice = Roll('scissors')
        elif cmd == 'f':
            User_choice = Roll('fire')

        print('Your choice is {}, Computer\'s choice is {}\n'.format(User_choice.name, PC_choice.name))

        api_log.trace('Your choice is {}, Computer\'s choice is {}\n'.format(User_choice.name, PC_choice.name))

        if User_choice.vs(PC_choice, dict[User_choice.name])==1:
            msg = "Round result: {} won, {} kills {}".format(player.name, User_choice.name, PC_choice.name)
            player.score+=1
        elif User_choice.vs(PC_choice, dict[User_choice.name])==-1:
            msg = "Round result: {} won, {} kills {}".format(computer.name, User_choice.name, PC_choice.name)
            computer.score+=1
        else:
            msg = "Draw, both {}".format(User_choice.name)
        api_log.trace(msg)
        count +=1

    if computer.score > player.score:
        print('{} is the winner'.format(computer.name))
    elif computer.score < player.score:
        print('{} is the winner'.format(player.name))
    else:
        print('Draw')
    msg = 'Score board: {}: {}\t\t{}: {}'.format(player.name, player.score, computer.name, computer.score)
    print(msg)
    api_log.trace(msg)


def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)

if __name__ == '__main__':
    init_logging(filename='Battle-history.log')
    main()