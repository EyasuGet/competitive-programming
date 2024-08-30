class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            curr = 0
            if i == "+":
                curr = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curr)
            elif i == "-":
                curr = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curr)
            elif i == "*":
                curr = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curr)
            elif i == "/":
                curr = int(float(stack[-2]) / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(curr))
            else:
                stack.append(int(i))
        return stack[-1]