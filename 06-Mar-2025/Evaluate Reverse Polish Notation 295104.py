# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {"+", "-","/","*"}
        stack = []

        for t in tokens:
            if t in operator:
                b, a = stack.pop(), stack.pop()
                curr = int(eval(str(a)+t+str(b)))
                stack.append(curr)
            else:
                stack.append(int(t))

        return stack[-1]