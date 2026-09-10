class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazine =  {}
        for c in magazine:
            count_magazine[c] = count_magazine.get(c, 0) + 1
        
        for c in ransomNote:
            count_magazine[c] = count_magazine.get(c, 0) - 1
            if count_magazine[c] < 0:
                return False

        return True