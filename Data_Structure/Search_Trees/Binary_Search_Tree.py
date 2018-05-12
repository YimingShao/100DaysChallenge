class Node:
    def __init__(self, k, v):
        self.left = None
        self.right = None
        self.parent=None
        self.k = k
        self.v = v

    def insert(self, k, v):
        if self.k:
            if k < self.k:
                if self.left is None:
                    self.left = Node(k, v)
                    self.left.parent=self
                else:
                    self.left.insert(k, v)
            elif k > self.k:
                if self.right is None:
                    self.right = Node(k, v)
                    self.right.parent = self
                else:
                    self.right.insert(k, v)
        else:
            self.v = v

    #this func is not completed yet
    def delete(self, k):
        self = self.search(k)
        subdict = {}
        if self.left is None:
            if self.right is None:
                if self is self.parent.left:
                    self.parent.left = None
                else:
                    self.parent.right = None
            else:
                self.parent.right = self.right

        elif self.right is not None and self.left is not None:
            temp = self
            self = self.left
            while self.right is not None:
                self = self.right
            temp.k=self.k
            temp.v=self.v
            temp.left.get_element(subdict)
            if temp.right:
                 temp.right.get_element(subdict)
            for k,v in subdict.items():
                print(k,v)
                temp.insert(k,v)



    def get_element(self, dict):
        if self.left:
            self.left.get_element(dict)
        dict.update({self.k:self.v})
        if self.right:
            self.right.get_element(dict)


    def search(self, k):
        if k < self.k:
            if self.left is None:
                return None
            return self.left.search(k)
        elif k > self.k:
            if self.right is None:
                return None
            return self.right.search(k)
        else:
            return self

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print('{} : {}'.format(self.k, self.v))
        if self.right:
            self.right.print_tree()


    def fill_in_dict(self, dict):

        if self.left:
            self.left.fill_in_dict(dict)

        sublist = []
        if self.left: sublist.append(str(self.left.k))
        if self.right: sublist.append(str(self.right.k))
        key = {self.k: sublist}
        dict.update(key)
        if self.right:
            self.right.fill_in_dict(dict)