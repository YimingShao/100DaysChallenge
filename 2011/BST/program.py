from api import BST
import random

def main():
    bst = BST()

    ary = [44,3,22,93,46,45,48,87,65,97]

    for i in range(0,10):
        bst.insert(ary[i])

    bst.printTree()
    bst.delete(44)
    bst.printTree()




if __name__ == '__main__':
    main()