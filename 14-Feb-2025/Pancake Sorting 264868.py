# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        sor = sorted(arr)

        n = len(sor) - 1

        ans = arr
        flips= []
        swap_i = 0
        while ans != sor and n >= 0:
            for i in range(len(ans)):
                if ans[i] == sor[n]:
                    swap_i = i


            flips.append(swap_i+1)

            ans[:swap_i+1] = ans[:swap_i+1][::-1]

            ans = ans[:n+1][::-1] + ans[n+1:]
            flips.append(n+1)
            n -= 1

        return flips