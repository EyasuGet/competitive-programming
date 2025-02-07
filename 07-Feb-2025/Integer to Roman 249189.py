# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            "1000": "M",
            "900": "CM",
            "500": "D",
            "400": "CD",
            "100": "C",
            "90": "XC",
            "50": "L",
            "40": "XL",
            "10": "X",
            "9": "IX",
            "5": "V",
            "4": "IV",
            "1": "I"
        }

        arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i = 0
        ans = []
        while i < len(roman) and num > 0:
            while arr[i] <= num:
                num -= arr[i]
                ans.append(roman[str(arr[i])])
            i += 1

        return "".join(ans)

