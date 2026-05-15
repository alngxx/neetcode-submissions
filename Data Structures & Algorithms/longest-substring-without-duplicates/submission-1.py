class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        longest = 0

        for r in range(len(s)):
            # if encounter duplicate, move left until no duplicate in window
            while s[r] in window:
                window.remove(s[l])
                l += 1

            length = r - l + 1                   # length of current substring
            longest = max(longest, length)       # update longest substring

            # expand window as right pointer move
            window.add(s[r])
        return longest      