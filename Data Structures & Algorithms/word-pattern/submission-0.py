class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # list of words
        words = s.split()
        if len(pattern) != len(words):
            return False

        p_to_w = {}     # {char : word}
        w_to_p = {}     # {word : char}

        # bijection check: if key already exists and value don't match, return False
        for i in range(len(words)):
            p = pattern[i]
            w = words[i]

            if p in p_to_w and p_to_w[p] != w:
                return False
            
            if w in w_to_p and w_to_p[w] != p:
                return False
            
            p_to_w[p] = w
            w_to_p[w] = p
        
        return True