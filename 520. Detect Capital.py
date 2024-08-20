class Solution(object):
    def detectCapitalUse(self, word):
        upper = word.upper()
        lower = word.lower()
        if upper == word:
            return True
        elif lower == word:
            return True
        else:
            return word.istitle()
        