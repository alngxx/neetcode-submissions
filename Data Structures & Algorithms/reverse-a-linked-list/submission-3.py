class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using three pointers
        # Initially
        # cur = 0 -> 1 -> 2 -> 3
        # prev = None

        prev = None  # prev always point to reversed LL
        cur = head   # iterate through the original LL

        while cur:
            # Save the next current node before reversing
            temp = cur.next
            # Reverse
            cur.next = prev
            # Move pointers forward after reversing
            prev = cur
            cur = temp
        
        return prev

            

        