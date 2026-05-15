class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            length = r - l + 1
            longest = max(longest, length)
            window.add(s[r])
        
        return longest

            

        