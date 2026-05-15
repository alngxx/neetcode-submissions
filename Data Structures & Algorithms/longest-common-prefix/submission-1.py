class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ Intuition: O(m x n)
        - Only need to compare with the first string
        - Take strs[0] as standard
        """

        for i in range(len(strs[0])):
            for s in strs:
                # if hit the end of any string, immediately return longest common prefix
                if i == len(s):
                    return s[:i]
                
                # or whenever find different char
                elif s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

            
            
        