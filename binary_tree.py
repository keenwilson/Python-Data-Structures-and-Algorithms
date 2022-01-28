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

    def traversePreOrder(self):
        self.__traversePreOrder(self.root)

    def __traversePreOrder(self, root):
        # Base condition to avoid the cycle
        if not root:
            return

        # Depth-First, Pre-order
        # Root, left, Right
        print(root.value)
        self.__traversePreOrder(root.leftChild)
        self.__traversePreOrder(root.rightChild)

    def traverseInOrder(self):
        self.__traverseInOrder(self.root)

    def __traverseInOrder(self, root):
        # Base condition to avoid the cycle
        if not root:
            return

        # Depth-First, In-order
        # Left, Root, Right
        self.__traverseInOrder(root.leftChild)
        print(root.value)
        self.__traverseInOrder(root.rightChild)

    def traversePostOrder(self):
        self.__traversePostOrder(self.root)

    def __traversePostOrder(self, root):
        # Base condition to avoid the cycle
        if not root:
            return

        # Depth-First, Post-order
        # Left, Right, Root
        self.__traversePostOrder(root.leftChild)
        self.__traversePostOrder(root.rightChild)
        print(root.value)

    # Depth
    # Calculate the depth by counting the number of edges
    # from root to target node

    def height(self):
        return self.__height(self.root)

    # Height
    # Find the longest path from the leaf node to the root node
    # The height of the tree = the height of the root node
    # Calculate the height of the left and right subtrees and add 1
    # 1 + max(height(L),height(R))
    # Post order traversal - visit the leaves first and pass the value up until we get the root node
    def __height(self, root):
        if not root:
            return -1
        # Base Condition
        if not root.leftChild and not root.rightChild:
            # The leaf node has 0 height
            return 0
        return 1 + max(self.__height(root.leftChild), self.__height(root.rightChild))

    def min(self):
        # Return the minimum value in a tree
        return self.__min(self.root)

    def __min(self, root: Node):
        # Base Condition
        if not root.leftChild and not root.rightChild:
            # The leaf node, return the value of that node
            return root.value
        left = self.__min(root.leftChild)
        right = self.__min(root.rightChild)

        return min(min(left, right), root.value)

    def equals(self, other):
        if not other:
            return False

        return self.__equals(self.root, other.root)

    def __equals(self, first: Node, second: Node):
        if not first and not second:
            return True
        if first and second:
            # Pre-order
            # Compare the root first, follow by the left, and right subtrees
            return (
                first.value == second.value
                and self.__equals(first.leftChild, second.leftChild)
                and self.__equals(first.rightChild, second.rightChild)
            )
        return False

    def getNodesAtDistance(self, distance: int):
        list = []
        self.__getNodesAtDistance(self.root, distance, list)
        return list

    def __getNodesAtDistance(self, root, distance: int, list):
        if not root:
            return
        if distance == 0:
            list.append(root.value)
            return
        # If we reach this point,
        # The distance is greater than zero
        # As we go down, we decrement the distance by 1
        self.__getNodesAtDistance(root.leftChild, distance - 1, list)
        self.__getNodesAtDistance(root.rightChild, distance - 1, list)


tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)
# print(tree.find(11))
# print(tree.traverseInOrder())
# print(tree.traversePreOrder())
# print(tree.traversePostOrder())
# print(tree.height())
# print(tree.min())
tree2 = Tree()
tree2.insert(7)
tree2.insert(4)
tree2.insert(9)
tree2.insert(1)
tree2.insert(6)
tree2.insert(8)
tree2.insert(10)
print("Equality Checking", tree.equals(tree2))
print("Nodes at distance", 2, tree.getNodesAtDistance(2))
