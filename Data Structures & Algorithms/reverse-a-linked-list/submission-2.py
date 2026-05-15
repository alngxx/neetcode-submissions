# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using three pointers
        # Initially
        # cur = 0 -> 1 -> 2 -> 3
        # prev = None

        prev = None
        cur = head

        while cur:
            # Save the next current node before reversing
            temp = cur.next
            # Reverse
            cur.next = prev
            # Move pointer forward
            prev = cur
            cur = temp
        
        return prev

            

        