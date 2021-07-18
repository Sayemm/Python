#https://www.youtube.com/playlist?list=PLV3rqOvr9vgkW7U-kdxtUBx74ICpw94k8
#each node has two nodes (left node and right node) except leaf node
#so insert is like BFS

from f_print_binary_tree import BinaryTreePrinter
from c_Queue import queue

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            q = queue()
            q.enque(self.root)

            while True:
                ck = q.deque()

                if ck.left is None:
                    ck.left = TreeNode(val)
                    return
                elif ck.right is None:
                    ck.right = TreeNode(val)
                    return
                else:
                    q.enque(ck.left)
                    q.enque(ck.right)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)

tree = BinaryTree()

tree.insert('a')
tree.insert('b')
tree.insert('c')
tree.insert('a')
tree.insert('b')
tree.insert('c')
tree.insert('c')

print(tree)

#      ....a....
#     /         \
#   .b.         .c.
#  /   \       /   \
# a     b     c     c