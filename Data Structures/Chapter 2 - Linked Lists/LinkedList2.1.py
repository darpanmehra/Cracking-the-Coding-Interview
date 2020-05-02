#2.1 - Remove Dups: Write Code to remove duplicates from an unsorted list
#RemoveDups() with buffer, RemoveDupsWithoutBuffer() without buffer space
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while(current.next):
                current=current.next
            current.next = newnode
    def printlist(self):
        if self.head is None:
            print("No List")
        else:
            current = self.head
            while (current):
                print(current.data)
                current = current.next

    def RemoveDups(self): #Time Complexity of O(n)
        current = self.head
        myset = set()
        while(current):
            if (current.data in myset):
                prev.next = current.next
            else:
                prev = current
                myset.add(current.data)
            current = current.next
    def RemoveDupsWithoutBuffer(self): #Time Complexity of O(n^2) and Space complexity of O(1)
        current = self.head
        while(current):
            checker = current
            while(checker.next):
                if (checker.next.data == current.data):
                    checker.next = checker.next.next
                else:
                    checker = checker.next
            current = current.next
if __name__ == "__main__":
    linklist = LinkedList()
    linklist.insert(2)
    linklist.insert(4)
    linklist.insert(1)
    linklist.insert(2)
    linklist.insert(2)
    linklist.RemoveDupsWithoutBuffer()
    linklist.printlist()
