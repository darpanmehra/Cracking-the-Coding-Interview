# 2.7 Intersection; Given two (singly) linked lists, determine if the two lists intersect.
# Return the inter- secting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference) as the j th node of the second linked list, then they are intersecting.
# Example:  List A -  9 6 8 4 5, List B -  6 1 5 8 4 5, Intersection = 8
class Solution:
    def findIntersection(self, headA, headB):
        if not headA or not headB:
            return None
        listA, listB = headA, headB
        lenA , lenB = 0,0
        while listA:
            lenA += 1
            listA = listA.next
        while listB:
            lenB += 1
            listB = listB.next
        listA, listB = headA, headB
        for _ in range(abs(lenA-lenB)):
            if lenA >= lenB:
                listA = listA.next
            else:
                listB = listB.next
        while listB != listA:
            listA, listB = listA.next, listB.next
        return listA
