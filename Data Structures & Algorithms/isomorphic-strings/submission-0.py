class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in map_s and map_s[c1] != c2) or (c2 in map_t and map_t[c2] != c1):
                return False
            map_s[c1] = c2
            map_t[c2] = c1
        return True