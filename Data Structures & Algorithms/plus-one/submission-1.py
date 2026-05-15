class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Turn list digits into integer num
        # Can use: num = int(".join(map(str, digits))")
        num = 0
        for digit in digits:
            num = num * 10 + digit

        num += 1
        
        res = []
        for i in str(num):
            res.append(int(i))

        return res
        