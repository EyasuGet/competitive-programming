from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        arr1 = dict(Counter(s))
        arr2 = dict(Counter(t))

        for ke,values in arr1.items():
            if ke not in arr2.keys():
                return False
            if arr2[ke] != values:
                return False


        return True
        