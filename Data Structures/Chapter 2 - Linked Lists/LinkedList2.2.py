#2.2 Return Kth element from the last in Singly Linked List
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        newnode = Node(data)
        if (self.head is None):
            self.head = newnode
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newnode
    def printlist(self):
        if self.head is None:
            print("No List")
        else:
            current = self.head
            while(current):
                print(current.data, end=" ")
                current = current.next
    def ReturnKthToLast(self, k): #Time Complexity O(n) and Space Complexity O(1)
        if self.head is None:
            print("No List")
            return
        fast = self.head
        slow = self.head
        for i in range(k):
            fast = fast.next
        while (fast.next):
            slow = slow.next
            fast = fast.next
        print(slow.data)

if __name__ == "__main__":
    linklist = LinkedList()
    linklist.insert(1)
    linklist.insert(5)
    linklist.insert(6)
    linklist.insert(2)
    linklist.insert(9)
    linklist.printlist()
    linklist.ReturnKthToLast(2)