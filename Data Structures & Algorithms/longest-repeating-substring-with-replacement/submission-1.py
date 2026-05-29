class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}      # dict count frequency of each character
        max_count = 0   # track most frequent character inside window - this is the one we don't want to be replaced
        res = 0 
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1    # update frequency of current character
            max_count = max(max_count, count[s[r]])

            # if window size > max_count + max number of replacements  
            # shrink window from the left
            if max_count + k < (r - l + 1):
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
        