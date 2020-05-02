#Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
#DEFINITION:
#Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
#EXAMPLE: Input: A->8->C->D->E-> C[the same C as earlier] Output: C
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
class Solution:
    def loopdetect(self):
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        slow = self.head
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return fast