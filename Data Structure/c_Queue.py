#https://www.youtube.com/playlist?list=PLV3rqOvr9vgkW7U-kdxtUBx74ICpw94k8

from collections import  deque
from a_Doubly_Linked_List import DoubleLinkedList

class queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enque(self, val):
        self.__list.add(val)

    def deque(self):
        val = self.__list.front()
        self.__list.remove_first()
        return  val

    def front(self):
        return self.__list.front()

    def __len__(self):
        return self.__list.size

# q = queue()
#
# q.enque(1)
# q.enque(2)
# q.enque(10)
# q.enque(5)
#
# print(len(q))
# print(q.front())
#
# q.deque()
#
# print(len(q))
# print(q.front())



