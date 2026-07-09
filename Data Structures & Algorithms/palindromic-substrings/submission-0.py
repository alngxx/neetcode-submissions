class Solution:
    def countSubstrings(self, s: str) -> int:
        """ 2D DP: O(n²), O(n²) - Simpler version of 5. Longest Palindrome
        1. dp[i][j] = True means substring s[i..j] is palindrome
        2. A substring dp[i][j] is palindrome if both:
        - two ends match: s[i] == s[j]
        - dp[i + 1][j - 1] already a palindrome
        3. Special case: if j - i <= 2, only need to compare s[i] == s[j]
        4. Fill bottom-up: i in range(n-1, 0); j in range (i, n)
        5. Whenever found a palindrome (dp[i][j] = True), count += 1
        """
        n = len(s)
        count = 0

        # 2D DP init = False
        dp = [[False] * n for _ in range(n)]

        # bottom-up
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1

        return count