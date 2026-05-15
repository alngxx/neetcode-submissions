# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle (slow pointer)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second halve then link node by node with first halve
        cur = slow.next  # Point to the head of second halve
        prev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Link first halve to second halve - node by node 
        first = head                # L0
        second = prev               # L(n)
        while second:
            # Save next node before link
            temp1 = first.next      # temp1 = L2
            temp2 = second.next     # temp2 = L(n-1)

            # Link node by node
            first.next = second     # L0 -> L(n)
            second.next = temp1     # L(n) -> L1

            first, second = temp1, temp2
        
        
        