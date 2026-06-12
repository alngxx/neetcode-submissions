"""
1. Use slow/fast to find middle
2. Reverse second half
3. Link first half - second half node by node
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle (slow pointer)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half then link node by node with first half
        cur = slow.next             # head of second half
        prev = slow.next = None     # cut the second half off (slow.next = None)
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Link first half to second half - node by node 
        first = head                # L0
        second = prev               # L(n)
        while second:
            # Save next node before link
            temp1 = first.next      # temp1 = L1
            temp2 = second.next     # temp2 = L(n-1)

            # Link node by node
            first.next = second     # L0 -> L(n)
            second.next = temp1     # L(n) -> L1

            first, second = temp1, temp2
        
        
        