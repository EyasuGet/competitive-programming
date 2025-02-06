# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = {"q","w","e","r","t","y","u","i","o","p"}
        row2 = {"a","s","d","f","g","h","j","k","l"}
        row3 = {"z","x","c","v","b","n","m"}

        ans = []
        for word in words:
            if word[0].lower() in row1:
                count = 0
                for i in word:
                    if i.lower() in row1:
                        count += 1  

                if count == len(word):
                    ans.append(word) 
            elif word[0].lower() in row2:
                count = 0
                for i in word:
                    if i.lower() in row2:
                        count += 1
                print(count)
                    
                if count == len(word):
                    ans.append(word) 
            else:
                count = 0
                for i in word:
                    
                    if i.lower() in row3:
                        count += 1
                    
                if count == len(word):
                    ans.append(word)
        return ans
                