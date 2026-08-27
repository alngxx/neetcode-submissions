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
            # e.g. "atc", "cat" has key = "act"
            key = "".join(sorted(s))

            # create empty group if key not yet in hashmap
            if key not in res:
                res[key] = []
            
            # add each string to its corresponding sorted key
            res[key].append(s)
        return list(res.values())