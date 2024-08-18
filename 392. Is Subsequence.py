class Solution(object):
    def isSubsequence(self, s, t):
        left = 0
        answer = ""
        if len(s) == 0:
            return True

        for i in t:
            if i == s[left] and left < (len(s)):
                answer += i
                left += 1
                if left == len(s):
                   return answer == s 
        return answer == s

        # two pointer approach
        # i, j =0, 0

        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
            
        # if i == len(s):
        #     return True
        # else:
        #     return False