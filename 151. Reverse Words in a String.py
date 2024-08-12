class Solution(object):
    def reverseWords(self, s):
        li = s.split()
        #for splitting the sentence into words
        left = 0
        right = len(li) - 1
        while left <= right:
            li[left], li[right] = li[right],li[left]
            left += 1
            right -= 1
        return " ".join(li)        
        