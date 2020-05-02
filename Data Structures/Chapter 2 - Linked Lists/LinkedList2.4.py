# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be after the elements less than x (see below).
# The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE: Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = tail1 = ListNode(0)
        head2 = tail2 = ListNode(0)
        while (head):
            if (head.val < x):
                tail1.next = head
                tail1 = tail1.next
            else:
                tail2.next = head
                tail2 = tail2.next
            head = head.next
        tail2.next = None
        tail1.next = head2.next
        return head1.next


