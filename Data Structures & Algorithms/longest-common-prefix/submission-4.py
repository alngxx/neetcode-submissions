class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ Intuition: O(m x n)
        - Only need to compare with the first string
        - Take strs[0] as standard
        """
        prefix = strs[0]
        for i in range(len(prefix)):
            for s in strs:
                # if hit end of any string, or hit unmatched char: return immediately
                if i == len(s) or prefix[i] != s[i]:
                    return s[:i]
        
        return prefix


            
            
        