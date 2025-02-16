# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        check = Counter(s1)

        window = defaultdict(int)

        for i in range(len(s1)):
            window[s2[i]] += 1
        
        if window == check:
            return True

        

        st = len(s1)
        left = 0
        for i in range(st,len(s2)):
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            
            left += 1
            window[s2[i]] += 1

            if window == check:
                return True
        return False
