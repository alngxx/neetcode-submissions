class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ Intuition: O(m x n)
        - Only need to compare with the first string
        - Take strs[0] as standard
        """
        prefix = strs[0]     # set strs[0] as a standard prefix

        for i in range(len(prefix)):
            for s in strs:
                # If hit the end of any string, immediately return longest common prefix
                if i == len(s):
                    return s[:i]
                # Return longest common prefix when unmatched appear
                if s[i] != prefix[i]:
                    return s[:i]
        return prefix


            
            
        