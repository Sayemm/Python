#https://www.youtube.com/playlist?list=PLV3rqOvr9vgkW7U-kdxtUBx74ICpw94k8
#Stack using Doubly Linked List
#Also possible using List

from a_Doubly_Linked_List import  DoubleLinkedList

class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size==0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size

s = Stack()

# s.push(1)
# s.push(5)
# print(s.peek())
#
# s.push(2)
# print(len(s))
#
# s.pop()
# print(len(s))
# print(s.peek())
