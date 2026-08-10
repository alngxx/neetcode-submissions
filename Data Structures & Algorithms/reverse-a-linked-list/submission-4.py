class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Three Pointers: prev, cur, temp
        # cur = 0 -> 1 -> 2 -> 3
        # prev = None

        prev = None     # prev always point to head of reverse list
        cur = head      # current pointer

        while cur:
            # save next node before reverse
            temp = cur.next
            # reverse: 0 -> None
            cur.next = prev
            prev = cur
            
            # move forward to next node
            cur = temp

        return prev