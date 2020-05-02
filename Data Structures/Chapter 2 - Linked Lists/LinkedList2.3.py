#2.3 Delete Middle Node: Algorithm to delete the middle node of linkedlist (i.e Any node but the first & last), given access to only that node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
class Solution:
    def RemoveNode(self, node):
        if (node is None or node.next is None):
            return False
        temp = node.next
        node.data = temp.data
        node.next = temp.next
