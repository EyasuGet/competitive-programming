# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while st and temperatures[st[-1]] < temperatures[i]:
                top = st.pop()
                ans[top] = i - top
            st.append(i)

        return ans