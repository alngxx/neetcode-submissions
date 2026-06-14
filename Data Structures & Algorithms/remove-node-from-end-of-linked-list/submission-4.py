class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ Two Pointers:
        Goal is to make second land on the (n+1) node from the end (right BEFORE target)
        1. first = second = head
        2. Move first to the (n+1) node from start
        3. Then move second along with first
        4. When first.next = None, second = (n+1) node from the end
        5. Remove target: second.next = second.next.next
        """
        dummy = ListNode(0, head)   # dummy.next = head in case head is removed
        first = second = dummy

        # Move first to (n+1) node from start (dummy) -- loop n times
        for _ in range(1, n+1):
            first = first.next

        # When first reach end (first.next = None), second land on the (n+1) node from end
        while first.next:
            first = first.next
            second = second.next

        # Now: first.next = None, second.next = target
        second.next = second.next.next      # remove target

        return dummy.next