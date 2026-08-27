class Solution:
    def isHappy(self, n: int) -> bool:
        def output(n):
            res = 0
            while n:
                digit = n % 10
                res += digit ** 2
                n //= 10
            
            return res
        
        visit = set()
        while n not in visit:
            visit.add(n)
            n = output(n)

        return True if 1 in visit else False