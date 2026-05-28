class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        longest = 0

        for r in range(len(s)):
            # if encounter duplicate, slide right until no duplicate in window
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])                   # add to window as slide right
            longest = max(longest, r - l + 1)  # update longest substring

        return longest