# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        str1 = s.split(" ")

        ans = []
        maxx = 0
        for i in str1:
            if len(i) > maxx:
                maxx = len(i)
        print(maxx)
        #the maximum length should be the index that we have to iterate

        ans = []
        for i in range(maxx):
            formed = []

            for j in range(len(str1)):
                if i < len(str1[j]):
                    formed.append(str1[j][i])
                else:
                    formed.append(" ")
            ans.append("".join(formed).rstrip())

        return ans
            

            
    


            



        