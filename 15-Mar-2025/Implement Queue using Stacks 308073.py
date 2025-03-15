# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []
 
    def push(self, x):
        self.st1.append(x)

        

    def pop(self):
        if not self.st1 and not self.st2:
            return -1
        
        for i in range(len(self.st1)):
            self.st2.append(self.st1.pop())
        n = self.st2.pop()

        for i in range(len(self.st2)):
            self.st1.append(self.st2.pop())
        return n

    def peek(self):
        return self.st1[0]
        

    def empty(self):
        return not self.st1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()