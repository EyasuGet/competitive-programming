class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ("A", "E","I", "O", "U", "a", "e", "i", "o", "u")
        arr = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                arr.append(s[i])
        arr.sort()
        r = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = arr[r]
                r += 1
        return "".join(s)


             