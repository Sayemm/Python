#https://www.youtube.com/playlist?list=PLV3rqOvr9vgkW7U-kdxtUBx74ICpw94k8
#Doubly Linked List (linking 'previous node' to the 'next node' and vice versa

class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)

        if(self.tail is None):
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def remove_node(self, node):
        self.size -= 1

        if node.prev is None: #first node check
            self.head = node.next
        else:
            node.prev.next = node.next #else link 'previous node' of node to the 'next node' of node

        if node.next is None: #last node
            self.tail = node.prev
        else:
            node.next.prev = node.prev #else link 'next node' of node to the 'previous node' of node

    def remove(self, val):
        node = self.head
        while node != None:
            if node.val==val:
                self.remove_node(node)
            node = node.next

    def remove_last(self):
        if self.tail is not None:
            self.remove_node(self.tail)
    def remove_first(self):
        if self.head is not None:
            self.remove_node(self.head)

    def back(self):
        return self.tail.val

    def front(self):
        return self.head.val

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"

# mylist = DoubleLinkedList()
#
# mylist.add(24)
# mylist.add(1)
# mylist.add(4)
# mylist.add(4)
# mylist.add(1)
# mylist.add(4)
# mylist.add(65)
#
# print(mylist)
# print(mylist.size)
#
# mylist.remove(4)
# print(mylist)
# print(mylist.size)
#
# mylist.remove_last()
# print(mylist)
# print(mylist.size)
#
# mylist.remove_first()
# print(mylist)
# print(mylist.size)