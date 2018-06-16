import api
import time

def main():
    ary1 = [2, 3, 4, 5, 6, 7, 8, 9]
    ary2 = [10, 11, 12, 23, 33, 1, 9]
    ary3 = [0,0 ,0 ,0 ,0 ,0 ,0, 9]

    result1 = api.disjoint1(ary1, ary2, ary3)
    result2 = api.disjoint2(ary1, ary2, ary3)


if __name__ == '__main__':
    main()