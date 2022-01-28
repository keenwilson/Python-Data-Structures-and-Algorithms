# Python program for bunary tree traversals

# A class that represents an individual node in a Binary Tree
from logging import root


class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return f"Node={self.value}"


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root.value)

    def insert(self, value):
        # If the tree is empty, set the root to the new node
        if not self.root:
            self.root = Node(value)
            print("self.root", self.root)
            return

        # Other scenario: find the parent of the new node
        # Start from the root node and traverse the tree until we find a target node
        current = self.root
        while True:
            if value < current.value:
                if not current.leftChild:
                    # Found the parent
                    current.leftChild = Node(value)
                    break

                current = current.leftChild
            else:
                if not current.rightChild:
                    # Found the parent
                    current.rightChild = Node(value)
                    break
                current = current.rightChild

    def find(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.leftChild
            elif value > current.value:
                current = current.rightChild
            else:
                return True
        return False


tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)
print(tree.find(11))
