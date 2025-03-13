# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.homeP = ListNode(homepage)

    def visit(self, url: str) -> None:
        curr = ListNode(url)
        self.homeP.next = curr
        curr.prev = self.homeP
        self.homeP = self.homeP.next

    def back(self, steps: int) -> str:
        # print(self.homeP.val)
        while steps and self.homeP and self.homeP.prev:
            self.homeP = self.homeP.prev
            steps -=1

        return self.homeP.val

    def forward(self, steps: int) -> str:
        while steps and self.homeP and self.homeP.next:
            self.homeP = self.homeP.next
            steps -= 1
        return self.homeP.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homeP)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)