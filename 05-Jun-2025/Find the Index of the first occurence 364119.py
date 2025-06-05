# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution(object):
    def strStr(self, haystack, needle):
        # l1 = 0
        # l2 = 0

        # for i in range(len(haystack)):
        #     if haystack[i] == needle[l2]:
        #         l2 += 1
                

        #     else:
        #         l1 = i
        #         l2 = 0
        # return -1


        # l1, l2 = 0, 0
        # while l1 < len(haystack):
        #     if haystack[l1] == needle[l2]:
        #         l2 += 1
        #         l1 += 1
        #         if l2 == len(needle):
        #             return l1 - len(needle)
                
        #     else:
        #         l1 += 1
        #         l2 = 0
        # return -1

        for i in range(len(haystack)):
            k = 0
            for j in range(i,len(haystack)):
                if haystack[j] == needle[k]:
                    k += 1
                else:
                    break
                if k == len(needle):
                    return i
        return -1

        