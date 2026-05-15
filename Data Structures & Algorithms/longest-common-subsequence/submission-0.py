class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """ DP Bottom-up 2D array
        - dp[i][j] = LCS(i, j) = length of LCS of text1[:i] and text2[:j]
        - When i = 0 or j = 0, one string is empty → dp[0][j] = dp[i][0] = 0
        - Thus, first row and first col stores these 0s

        DP Bottom-up Algorithm:
        - Compare text1[i] and text2[j] one by one
        - If equal → LCS(i, j) = LCS(i-1, j-1) + 1
        - Else → LCS(i, j) = max(LCS(i−1, j), LCS(i, j−1))
        """

        n = len(text1)
        m = len(text2)
        dp = [ [0] * (m + 1) for _ in range (n + 1)]  # (n+1)(m+1) DP array

        # Compare every char of each text one by one
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # LCS of text1[:n] = text1 and text2[:m] = text2
        return dp[n][m]