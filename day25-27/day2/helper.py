import os
import datetime

def main():
    menu()
    key = rec_input()
    if key is '1':
        dir_name = input('Input the dir name:\t')
        make_dir(dir_name)
    elif key is '2':
        file_name = input(('Input the file name:\t'))
        make_file(file_name)
    else:
        make_challenge_dir()




def make_dir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError as fee:
        print('Error: Director exists')

def make_file(file):
    f = open(file, 'w+')

def make_challenge_dir():
    first_day = datetime.datetime(2018, 4, 13)
    num1 = int((datetime.datetime.now()-first_day).days)+3
    if ((num1-1)% 3)!=0:
        th_day = 'Second'
        if num1 %3 ==0:
            th_day = 'third'
        print('Today is the {} day of your current challenge'.format(th_day))
        return
    num2 = num1+2
    try:
        dir_name = 'day{}-{}'.format(num1, num2)
        os.mkdir(dir_name)
        os.chdir(dir_name)
        for i in range(1,4):
            os.mkdir('day{}'.format(i))
        os.chdir(os.getcwd())

    except FileExistsError as fee:
        print('Error: Director for today exist')





def menu():
    print('---------------------------------')
    print('          Dir_files_creater')
    print('---------------------------------')
    print('1: make dir')
    print('2: make file')
    print('3: make challenge dir')
    print()

def rec_input():
    key = input('Insert 1, 2 or 3:\t')
    collection = ['1', '2', '3']
    if key not in collection:
        return rec_input()
    return key

if __name__ == '__main__':
    main()