class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        1. Brute force: return sorted(s) == sorted(t)
        -> O(nlogn) since we have to sort

        2. HashMap: O(n)
        Use two HashMaps to store frequency of each character
        key = character
        value = frequency
        '''
        # Anagrams must have same length
        if len(s) != len(t):
            return False
        
        # Dicts store character frequencies of s and t
        countS = {}
        countT = {}

        # dict[key] = value
        # Count frequency of each character in both strings
        # dict.get(key, default) returns the value if key exists, 
        # otherwise returns the default (here 0)

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1   # Increment 1 for each count
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        return countS == countT


        
        