import random
from lib import (Selection_Sort)


def main():
    test1 = testing_ary()
    print('Before: {}'.format(test1))
    Selection_Sort(test1)
    print('After: {}'.format(test1))

def testing_ary():
    return (random.sample(range(0,100), 20))



if __name__ == '__main__':
    main()