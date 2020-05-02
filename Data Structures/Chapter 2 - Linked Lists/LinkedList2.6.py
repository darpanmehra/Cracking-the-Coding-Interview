#2.6 Check if the LinkedList is a Palindrome
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList():
    def __init__(self):
        self.head = None
    def insert(self, data):
        newnode = Node(data)
        if (self.head is None):
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def printll(self):
        if self.head is None:
            print("No list")
        else:
            current = self.head
            while(current):
                print(current.data)
                current = current.next
    def PalindromeUsingStackSlicing(self):
        current = self.head
        stack = []
        while current:
            stack.append(current.data)
            current = current.next
        return stack == stack[::-1]
    def PalindromeUsingStack(self):
        if self.head is None:
            return True
        fast = slow = self.head
        stack = []
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        while(slow):
            stack.append(slow.data)
            slow = slow.next
        current = self.head
        while(stack):
            if (stack.pop() != current.data):
                return False
            current = current.next
        return True
    def PalindromeByReversing(self):
        fast = slow = self.head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        prev = None
        while (slow):
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        current = self.head
        while prev:
            if (prev.data != current.data):
                return False
            prev = prev.next
            current = current.next
        return True

if __name__=="__main__":
    linklist = LinkedList()
    linklist.insert(1)
    linklist.insert(2)
    linklist.insert(2)
    linklist.insert(3)
    print("Yes") if linklist.PalindromeByReversing() else print("NO")