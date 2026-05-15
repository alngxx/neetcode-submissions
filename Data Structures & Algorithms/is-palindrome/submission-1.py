class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Intuition
        - Two pointers i and j: i = 0; j = len - 1
        - i forwards and j backwards, skip non-alphanumeric chars
        - if s[i].lower() != s[j].lower(): return False
        '''

        i, j = 0, len(s)-1
        while i < j:
            # Skip if s[i] is non-alphanumeric. while i < j make sure pointers in boundary
            while i < j and not s[i].isalnum():
                i += 1
            # Similar for s[j]
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        
        return True
        