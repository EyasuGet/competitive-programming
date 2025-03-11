# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        ans = 0
        for i in s:
            if i == "(":
                st.append(ans)
                ans = 0
            else:
                ans = st[-1] + max(ans * 2 , 1)
                st.pop()
        return ans