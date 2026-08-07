class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ Two Pointers: O(n)
        - i forwards and j backwards, skip non-alphanumeric chars
        - if s[i].lower() != s[j].lower(): return False
        """
        l, r = 0, len(s) - 1
        while l < r:
            # skip non-alphanumeric chars
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # if find unmatched pair, early exit
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        