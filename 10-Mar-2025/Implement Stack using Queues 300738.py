# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        
        self.que = []
    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        return self.que.pop()

    def top(self) -> int:
        return self.que[-1]

    def empty(self) -> bool:
        return not self.que
            


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()