#https://www.youtube.com/playlist?list=PLV3rqOvr9vgkW7U-kdxtUBx74ICpw94k8
#smaller value to the left node and bigger value to the right node
#insert like DFS

from f_print_binary_tree import BinaryTreePrinter
from b_Stack import Stack

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class BST:
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node is None: return

        if node.val == value: return #only unique value in BST
        elif node.val > value:
            if node.left is None:
                node.left = TreeNode(value)
                return
            else: self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return
            else : self.__insert_value(node.right, value)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_value(self.root, val)

    def __str__(self):
        tree_print = BinaryTreePrinter()
        return tree_print.get_tree_string(self.root)

    def __in_order(self, node): #print in ascending order
        if node is None: return
        self.__in_order(node.left)
        print(node.val, end=' ') #not found any node to the left then print the value of the node
        self.__in_order(node.right)

    def in_order(self): #print in ascending order
        self.__in_order(self.root)

    def contains(self, val):
        st = Stack()
        st.push(self.root)

        while not st.is_empty():
            node = st.pop()

            if node.val == val: return  True
            elif val < node.val:
                if node.left is not None: st.push(node.left)
            else:
                if node.right is not None: st.push(node.right)
        return False


tree = BST()

tree.insert(6)
tree.insert(7)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(3)

print(tree)
tree.in_order()

print()
print(tree.contains(4))
print(tree.contains(10))

#   ..........6.
#  /            \
# 1.             7
#   \
#    2....
#         \
#         .4
#        /
#       3
# 1 2 3 4 6 7
# True
# False