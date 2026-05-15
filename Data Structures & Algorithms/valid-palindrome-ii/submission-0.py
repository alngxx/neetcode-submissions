class Solution:
    def validPalindrome(self, s: str) -> bool:
        """ 
        Intuition: Two pointers -> O(n)
        - Function is_palindrome(i, j) to check whether a string from left to right is palindrome
        - In string s, whenever we found s[i] != s[j], check if we skip/remove i or j, the remaining string is_palindrome()
        """
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True
        
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                # Check if we remove i or j, the remaing string still palindrome
                return (is_palindrome(i + 1, j) 
                        or is_palindrome(i, j - 1))
            i += 1
            j -= 1

        return True
                

                