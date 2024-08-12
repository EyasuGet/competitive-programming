class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        l1 = len(str1)
        l2 = len(str2)
        answer = []

        if str1[0] != str2[0] or ((str1 + str2) != (str2 + str1)):
            return ""
        
        if l1 > l2:
            gc= math.gcd(l1,l2)
        else:
            gc = math.gcd(l2,l1)
        return str1[:gc]