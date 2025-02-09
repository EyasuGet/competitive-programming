# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        tot = 0

        for word in words:
            for i in word:
                if chars.count(i) < word.count(i):  #if any of the letters count is greater than what is in chars we will break our loop
                    break
            else:
                tot += len(word)
        return tot
        
        