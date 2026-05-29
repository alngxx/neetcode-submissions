class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """ Sliding Window
        Intuition: characters NOT the most frequent are the ones we want to replace
        Thus, we track:
        1. count - frequency of character
        2. max_count - most frequent character in window
        """

        count = {}
        l = 0
        max_count = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1   
            # update most frequency character in window
            max_count = max(max_count, count[s[r]])  

            window = r - l + 1
            # if window size > max_count + max_number_of_replacements, shrink it
            if window > max_count + k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)   # update longest substring
        return res