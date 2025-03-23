# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        comb = []
        start = 1
        def bt(start, comb):
            if start > n + 1:
                return 

            if len(comb) == k:
                ans.append(comb[:])
                return 

            comb.append(start)
            bt(start + 1, comb)
            comb.pop()
            bt(start + 1,comb)

        bt(start, comb)
        return ans





        # lst = list(range(1, n + 1))
        # return [list(comb) for comb in itertools.combinations(lst, k)]


