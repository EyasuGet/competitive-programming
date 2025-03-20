class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_count = Counter(t)
        s_count = Counter(s)

        if t_count == s_count:
            return 0

        ans = 0
        for key,val in s_count.items():
            if val > t_count[key]:
                ans += abs(t_count[key] - val)
        return ans
            
