class Solution:
    def longestPalindrome(self, s: str) -> str:
        """     2D DP: O(n²), O(n²)
        1. dp[i][j] = True means substring s[i..j] is a palindrome
        2. A substring is a palindrome if:
        - ends match: s[i] == s[j]
        - AND the inside is also a palindrome: dp[i+1][j-1]
        3. Special case: if length is 1, 2, or 3 (j - i <= 2), matching ends
        is enough — the inside is empty or a single char, always a palindrome
        4. Fill dp bottom-up: i goes from n-1 down to 0, j goes from i to n-1
        (this order guarantees dp[i+1][j-1] is already computed before dp[i][j])
        5. Track the longest palindrome found while filling
        """
        n = len(s)
        index = length = 0

        dp = [[False] * n for _ in range(n)]    # 2D dp[n][n] init = False

        # bottom-up
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i  <= 2 or dp[i + 1][j - 1] == True):
                    dp[i][j] = True
                    # update longest palindrome substring
                    if length < j - i + 1:
                        length = j - i + 1
                        index = i
        
        return s[index : index + length]
