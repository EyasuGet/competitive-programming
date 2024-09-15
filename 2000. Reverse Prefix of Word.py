class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        word = list(word)
        r = 0
        while r < len(word):
            if word[r] != ch:
                r += 1
            else:
                break
        
        l = 0

        while l < r:
            word[l] ,word[r] = word[r], word[l]

            l += 1
            r -= 1
        return "".join(word)