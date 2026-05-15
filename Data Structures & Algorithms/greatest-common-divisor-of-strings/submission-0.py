class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenating in different orders gives different results,
        # then no common divisor string exists.
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd_nums(a,b):
            # List stores all common divisors
            common_div = []
            for d in range (1, max(a,b)+1):
                # If d is a common divisor, append to list
                if a % d == 0 and b % d == 0:
                    common_div.append(d)

            # Return max d, which is GCD
            return max(common_div)

        d = gcd_nums(len(str1), len(str2))

        return str1[:d]

