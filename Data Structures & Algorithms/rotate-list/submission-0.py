class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ Circular list + cut off: O(n), O(1)
        1. Find length n, connect tail to head (circular), handle k %= n
        2. Walk n - k - 1 steps from head to find the new tail
        3. New head is new_tail.next; break the circle there
        """
        if not head or not head.next:
            return head

        tail, n = head, 1
        while tail.next:
            tail = tail.next
            n += 1
        
        # if k % n == 0, need not to rotate
        k %= n
        if k == 0:
            return head
        
        # connect tail -> head, make list circlar
        tail.next = head

        # find new_tail (move new_tail to 3)
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        # connect new_head, and cut off circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head