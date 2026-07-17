""" Linked List store numbers in reverse order, thus first nodes are the last digits
Thus, calculation is straightforward:
1. Add two digits from l1 and l2
2. Add carry from previous step
3. Save res = sum % 10 as new node
4. Update carry = sum // 10 for next calculation
5. Move pointers to next nodes
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # dummy.next = result list
        cur = dummy
        carry = 0

        # loop until both lists empty or no carry remains
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            # calculate new digit and carry
            sum = digit1 + digit2 + carry
            carry = sum // 10
            res = sum % 10
            cur.next = ListNode(res)    # save res as new node

            # move to next digits from l1 & l2
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next