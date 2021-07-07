'''
implementing inorder binary search tree traversal 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, num):
        if num == self.data:
            return
        else:
            if num < self.data:
                if self.left is None:
                    self.left = Node(num)
                else:
                    self.left.add_child(num)
            else:
                if self.right is None:
                    self.right = Node(num)
                else:
                    self.right.add_child(num)

    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print(self.data)
        if self.right:
            self.right.inorder_print()

if __name__ == "__main__":
    root = Node(10)
    root.add_child(5)
    root.add_child(15)
    root.add_child(20)
    root.add_child(18)
    root.add_child(22)

    print(root.inorder_print())

