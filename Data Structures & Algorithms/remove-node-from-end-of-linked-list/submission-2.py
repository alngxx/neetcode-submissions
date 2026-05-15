# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        # From now, nodes is a list stores references to each node in LL
        
        remove_index = len(nodes) - n
        # Special case: If removeIndex is head, return head.next as new head
        if remove_index == 0: 
            return head.next

        # Link previous node to next node after removed node
        nodes[remove_index-1].next = nodes[remove_index].next

        return head
