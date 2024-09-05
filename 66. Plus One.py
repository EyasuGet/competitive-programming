class Solution(object):
    def plusOne(self, digits):  
        num = ""
        for i in digits:
            num += str(i)
        n = int(num) + 1
        n = str(n)
        answer = []
        for i in n:
            answer.append(int(i))
        return answer

        