# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        else:
            self.q.appendleft(value)
            self.size += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        else:
            self.q.append(value)
            self.size += 1
            return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        else:
            self.q.popleft()
            self.size -= 1
            return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        else:
            self.q.pop()
            self.size -= 1
            return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.q[0]

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.q[-1]

    def isEmpty(self) -> bool:
        return self.size == 0
            

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()