class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_count = Counter(t)
        s_count = Counter(s)


        found = set()
        if t_count == s_count:
            return 0
        ans = 0
        for key, val in s_count.items():
            if key not in t_count:
                ans += val
            elif key not in found:
                found.add(key)
                ans += abs(t_count[key] - val)
            
        for key, val in t_count.items():
            if key not in s_count:
                ans += val
            elif key not in found:
                found.add(key)
                ans += abs(s_count[key] - val)
        return ans


        # res = 0
        # for char in "abcdefghijklmnopqrstuvwxyz":
        #     res += abs(s.count(char) - t.count(char))
        # return res