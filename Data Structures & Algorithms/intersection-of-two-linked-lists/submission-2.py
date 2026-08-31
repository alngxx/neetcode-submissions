# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ Two Pointers cycle trick: O(n + m), O(1)
        1. l1 = headA, l2 = headB
        2. When a pointer reaches end, set it to the other head
        3. Both pointers travel same total distance (a + b + c), meet at intersection or None
        Proof: lenA = a + c, lenB = b + c
        - l1 travel = (a + c) + b = intersecion
        - l2 travel = (b + c) + a = intersection
        What if don't exist intersecion, then c = 0, both pointers reaches None of the other list
        """
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        # return l1 (which equals l2), the intersection or None
        return l1
        
        
        