# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ Two pointers cycle trick: O(n + m), O(1)
        1. l1 starts at headA, l2 starts at headB
        2. When l1 reaches end, redirect to headB; when l2 reaches end, redirect to headA
        3. Both pointers travel same total distance (lenA + lenB), meet at intersection or None
        """
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        # return l1 (which equals l2), the intersection or None
        return l1
        
        
        