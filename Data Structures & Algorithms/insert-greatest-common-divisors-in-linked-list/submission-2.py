class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        # O(log n)
        def gcd(a, b):
            # 1. GCD(a, b) = GCD(b, remainder)
            # 2. Remainder has same GCD as a, b
            # 3. Repeat until remainder = 0
            # 4. At that moment, return a as GCD: GCD(a, 0) = a
            while b:
                a, b = b, a % b
            return a
        
        cur = head
        while cur and cur.next:
            temp = cur.next                                 # save next node
            gcd_node = ListNode(gcd(cur.val, temp.val))     # gcd node to insert
            # insert: cur -> gcd_node -> temp
            cur.next = gcd_node
            gcd_node.next = temp

            # advance cur
            cur = temp
            
        return head