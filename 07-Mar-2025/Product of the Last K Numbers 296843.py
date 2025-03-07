# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.arr = []
        self.suff = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = []
            self.suff = [1]
        else:
            self.arr.append(num)
            self.suff.append(self.suff[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.suff) - 1:
            return 0
        return self.suff[-1] // self.suff[-(k + 1)]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)