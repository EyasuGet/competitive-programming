# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)
        arr = freq.items()
        arr = sorted(arr, key = lambda a : a[1], reverse = True)
        ans = []
        for char, val in arr:
            ans.append(char*val)
        return "".join(ans)

        

        