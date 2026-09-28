class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ 1D DP, backwards: O(n * m * k), O(n)
        1. dp[i] = whether s[i:] can be segmented, dp[n] = True (empty string is valid)
        2. Walk i backwards, try every word in wordDict if it's in s[i:]
        3. If word matches and dp[i+len(word)] is True, set dp[i] = True
        4. Return dp[0]
        """
        n = len(s)

        # dp[i] = True if s[i:] can be segmented
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            # if a valid word appear in s[i:], update dp[i] = dp[i + len(w)]
            for w in wordDict:
                if i + len(w) <= n and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # if become True, break early - need not to try other word
                if dp[i]:
                    break
        return dp[0]