""" Brute Force: linked list -> array
    O(1) space solution
1. Use slow/fast to find middle element
2. Reverse the second half in-place
3. Traverse the two halves simultaneously, update max_sum
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find middle element
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the second half (head = slow)
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # Now, prev is head of second half
        
        # 3. Traverse the two halves at the same time
        max_sum = float("-inf")
        first, second = head, prev
        while second:
            cur_sum = 0
            cur_sum += (first.val + second.val)
            max_sum = max(max_sum, cur_sum)

            first, second = first.next, second.next
        
        return max_sum