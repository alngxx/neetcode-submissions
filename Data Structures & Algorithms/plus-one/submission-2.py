class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Turn list digits into integer num
        """
        num = int("".join(map(str, digits)))
        """
        num = 0
        for digit in digits:
            num = num * 10 + digit

        num += 1
        
        # Append every digit of num + 1 into res
        res = []
        for i in str(num):
            res.append(int(i))

        return res
        