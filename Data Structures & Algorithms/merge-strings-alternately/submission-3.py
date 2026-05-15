class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n1 = len(word1)
        n2 = len(word2)

        i, j = 0, 0

        while i < n1 and j < n2:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        if n1 > n2:
            res.extend(word1[n2:])
        if n2 > n1:
            res.extend(word2[n1:])

        string = "".join(res)

        return string



        
        