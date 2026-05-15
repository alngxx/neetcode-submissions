class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dict e.g. res = { ('a','e','t'): ['eat', 'tea'] }
        res = defaultdict(list)
        # key = tuple contain characters build up the anagram in sorted order
        # value = list of anagrams make up from that key

        # Iterate through every string in strs, then split them into different groups
        for s in strs:
            # dict's key can't be a list, but tuple is ok!
            key = tuple(sorted(s))
            res[key].append(s)
        
        # Return only dict's value
        return list(res.values())
        