# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = []
        cur = head
        # Traverse entire list while don't check next node (cur.next)
        while cur:
            node.append(cur.val)
            cur = cur.next
        
        return node == node[::-1]

        