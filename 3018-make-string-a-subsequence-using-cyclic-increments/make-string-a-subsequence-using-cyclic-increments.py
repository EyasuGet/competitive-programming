class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        # if len(str1) == len(str2) == 1:
        #     if str1 == str2:
        #         return True
        #     else:
        #         return (ord(str1[0])+1) == ord(str2[0])
        l1 = 0
        l2 = 0
        while l1< len(str1) and l2 < len(str2):
            if str1[l1] == str2[l2]:
                l1 += 1
                l2 += 1
            # elif (abs(ord(str1[l1]) - ord(str2[l2])) == 1 or (abs(ord(str1[l1]) - ord(str2[l2])) == 25)):
            elif ((ord(str1[l1]) + 1) == ord(str2[l2])) or (ord(str1[l1]) - 25 == ord(str2[l2])):
                l1 += 1
                l2 += 1
            else:
                l1 +=1

        return l2 >= len(str2)
        