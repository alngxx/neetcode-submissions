class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram must have same length
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        # dict[key] = value
        # dict.get(key, default value)
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        
        return True


        