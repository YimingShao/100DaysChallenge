from data import us_state_abbrev, states_list
from collections import OrderedDict
import sys
import subprocess




def main():
    menu()
    ordereddict = OrderedDict(us_state_abbrev)
    key = rec_input()
    while(key is not '6'):
        if key =='1':
            print_nth_item(states_list, ordereddict)
        if key=='2':
            print_nth_key_dict(ordereddict)
        if key=='3':
            print_nth_value_dict(ordereddict)
        if key=='4':
            repalce_item(states_list, ordereddict)
        if key=='5':
            surprise()
        key = rec_input()
    quit_program()


def rec_input():
    key = input("Insert a number: ")
    if(key.isdigit() is False or int(key) > 6 or int(key)<1):
        print("Invalud, try it again")
        return rec_input()
    return key

def quit_program():
    print('-' *71  + '\n')
    print('Bye Bye!')
    print('\n' + '-' * 71)
    sys.exit()


def print_nth_item(List, ordereddict):
    n = input('Input n: ')
    while(n.isdigit() is False or int(n)>len(states_list)-1 or int(n)<0):
        print("Invalid")
        n = input('Input n: ')

    itemdict = list(ordereddict.items())[int(n)]
    itemlist = List[int(n)]
    print('Number '+str(n)+' item in list is ' + itemlist+ '. Number '+str(n)+' item in dict is '+
    str(itemdict))


def print_nth_key_dict(ordereddict):
    n = input('Input n: ')
    while(n.isdigit() is False or int(n)>len(states_list)-1 or int(n)<0):
        print("Invalid")
        n = input('Input n: ')
    nthkey=list(ordereddict.keys())[int(n)]
    print('nth key in dict is '+str(nthkey))


def print_nth_value_dict(ordereddict):
    n = input('Input n: ')
    while(n.isdigit() is False or int(n)>len(states_list)-1 or int(n)<0):
        print("Invalid")
        n = input('Input n: ')
    nthvalue=list(ordereddict.values())[int(n)]
    print('nth value in dict is ' + str(nthvalue))


def repalce_item(mylist,ordereddict):
    n1 = input('Input n1: ')
    while(n1.isdigit() is False or int(n1)>len(states_list)-1 or int(n1)<0):
        print("Invalid")
        n1 = input('Input n1: ')
    n2 = input('Input n2: ')
    while(n2.isdigit() is False or int(n2)>len(states_list)-1 or int(n2)<0):
        print("Invalid")
        n2 = input('Input n2: ')

    n1=int(n1)
    n2=int(n2)
    oldname = list(ordereddict.keys())[n1]
    newname=mylist[n2]
    ordereddict[newname]=ordereddict.pop(oldname)

    print('updated')


def surprise():
    subprocess.call(['java','-jar','Surprise.jar'])


def menu():
    line = '-' * 30
    print(line + 'Instruction' + line)
    print('Insert 1: Print out the nth item in each.')
    print('Insert 2: print out the nth key in the dictionary.')
    print('Insert 3: Print out the nth value in the dictionary.')
    print('Insert 4: Replace the n1th key in the dictionary with the n2th item in the list.')
    print('Insert 5: Surprise.')
    print('Insert 6: Quit.')
    print('Note: the range of the dictionary and the list si 0~'+ str(len(states_list)-1))
    print(line + line + '-' * 11)

if __name__ == '__main__':
    main()