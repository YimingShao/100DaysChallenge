class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True


    # The worst case of searching is the depth of the tree.
    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()

            print(str(self.value))

            if self.right:
                self.right.inorder()


    def printTree(self):
        if self:
            rightv = 'None'
            leftv = 'None'
            if self.right:
                rightv = str(self.right.value)
            if self.left:
                leftv = str(self.left.value)
            print("{}: left: {}, right: {}".format(str(self.value), leftv, rightv))
            if self.left:
                self.left.printTree()
            if self.right:
                self.right.printTree()




class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is None:
            return False


        # data is in root node
        if self.root.value == data:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                delNodeParent = self.root
                delNode = self.root.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left

                self.root.value = delNode.value
                if delNode.right:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.left = delNode.right
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.right = delNode.right
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None
            return True
        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.left
            elif data > node.value:
                node = node.right

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove node has no children
        elif node.left is None and node.right is None:
            if data < parent.value:
                parent.left = None
            else:
                parent.right = None
            return True

        # case 3: remove node has left child only
        elif node.left and node.right is None:
            if data < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        # case 4: remove node has right child only
        elif node.left is None and node.right:
            if data < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        # case 5: remove node has left and right children
        else:
            delNodeParent = node
            delNode = node.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left

            node.value = delNode.value
            if delNode.right:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = delNode.right
                elif delNode.value < delNode.value:
                    delNodeParent.right = delNode.right
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None


    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def printTree(self):
        print("The tree")
        self.root.printTree()
        print("")


    def preorder(self):
        print("PreOrder")
        self.root.preorder()
        print("")

    def postorder(self):
        print("PostOrder")
        self.root.postorder()
        print("")

    def inorder(self):
        print("InOrder")
        self.root.inorder()
        print("")

