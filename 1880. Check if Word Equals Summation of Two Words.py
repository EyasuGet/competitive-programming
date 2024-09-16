class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def order(x):
            l = ""
            for i in x:
                l += str((ord(i) - 97))
            return int(l)


        c1 = order(firstWord)
        c2 = order(secondWord)
        c = order(targetWord)
        return c == c1 + c2
        