class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ Hashmap with sorted string as key: O(n * k logk), O(n * k)
        where k = max length of a string
        1. Sort each string to know its anagram key
        2. Group strings share same key together
        3. Return list of groups
        """
        res = {}
        for s in strs:
            # anagrams share same sorted key
            # e.g. "eat", "tea", "ate" all sort to "aet"
            key = "".join(sorted(s))

            # if sorted key not in hashmap, create empty group for it
            if key not in res:
                res[key] = []

            # add every string to its anagram group
            res[key].append(s)
        
        return list(res.values())
        