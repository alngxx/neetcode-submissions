class Solution:
    def intToRoman(self, num: int) -> str:
        # O(1), O(1)
        # 1 <= num <= 3999
        roman = {
            1000: "M", 900: "CM",
            500: "D", 400: "CD",
            100: "C", 90: "XC",
            50: "L", 40: "XL",
            10: "X", 9: "IX",
            5: "V", 4: "IV",
            1: "I",
        }
        res = ""
        for val in roman:
            count = num // val      # quotient: e.g. 3
            if count > 0:
                res += roman[val] * count
                num = num % val     # remainder: e.g. 749
        return res