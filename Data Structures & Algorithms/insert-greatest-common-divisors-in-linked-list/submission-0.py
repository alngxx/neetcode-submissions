# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        def gcd(a, b):
            # O(log n)
            # GCD(a, b) = GCD(b, a % b)
            # a % b share same GCD as a, b
            # repeat until remainder, or b = 0
            # and return a, since GCD(a, 0) = a
            while b:
                a, b = b, a % b
            return a
        
        cur = head
        while cur and cur.next:
            temp = cur.next
            cur.next = ListNode(gcd(cur.val, temp.val))
            cur.next.next = temp
            cur = temp

        return head