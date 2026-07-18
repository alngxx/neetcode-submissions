"""
1. Find prev_left to reconnect the list after reverse
2. Reverse the sublist
3. Reconnect both ends
head = [1,2,3,4,5], left = 2, right = 4
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)       # dummy.next = head
        prev_left = dummy               
        cur = head                      # cur = 1

        # 1. Move prev_left.next = cur = left
        for _ in range(1, left):
            prev_left = prev_left.next
            cur = cur.next
        # Now: prev_left = 1, cur = 2

        # 2. Reverse from left - right
        prev = None
        for _ in range(left, right + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # Now: prev = 4, cur = 5

        # 3. Reconnect both ends: 2-5, 1-4
        prev_left.next.next = cur   # prev_left.next = 2, cur = 5
        prev_left.next = prev       # prev_left = 1, prev = 4

        return dummy.next