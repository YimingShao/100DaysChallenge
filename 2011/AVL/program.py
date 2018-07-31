from api import AVL_Tree
def main():
    myTree = AVL_Tree()
    root = None

    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

    print("Preorder traversal of the",
          "constructed AVL tree is")
    myTree.preOrder(root)
    print()


if __name__ == '__main__':
    main()