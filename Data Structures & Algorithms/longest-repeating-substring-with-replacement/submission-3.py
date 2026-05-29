class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """ Intuition: Sliding Window
        The characters NOT the most frequent are the ones we want to replace
        Thus, we track:
        1. count - dict count frequency of each character
        2. max_count - most frequent character inside window - this is the one we want don't want to replace
        """
        count = {} 
        max_count = 0   # track most frequent character inside window - this is the one we don't want to be replaced
        res = 0 
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1    # update frequency of current character
            max_count = max(max_count, count[s[r]])

            # if window size > max_count + max number of replacements  
            # shrink window from the left
            if (r - l + 1) > max_count + k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
        