class Solution(object):
    def reverseVowels(self, s):
        li = list(s)
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        left = 0
        right = len(s) - 1
        while left <= right:
            if li[left] in vowels and li[right] in vowels:
                li[left],li[right] = li[right],li[left]

                left += 1
                right -= 1
            elif li[right] not in vowels and li[left] in vowels:
                right -= 1
            elif li[left] not in vowels and li[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(li)
        