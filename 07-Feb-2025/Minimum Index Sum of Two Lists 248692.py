# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq1 = {}
        for idx,str1 in enumerate(list1):
            freq1[str1] = idx
        
        ans = []
        min_sum = float("inf")
    
        for i in range(len(list2)):
            if list2[i] in freq1:
                if i + freq1[list2[i]] < min_sum:
                    ans.clear()
                    ans.append(list2[i])
                    min_sum = i + freq1[list2[i]]
                elif i + freq1[list2[i]] == min_sum:
                    ans.append(list2[i])
        return ans
                    
        

        
