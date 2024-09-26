class Solution(object):
    def strStr(self, haystack, needle):
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

        