class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        circular = code + code
        n = len(code)
        ans = [0] * n
        for i in range(n):
            j = k
            if j >= 0:
                curr = 0
                c = i + 1
                
                while j > 0:
                    curr += circular[c]
                    c += 1
                    j -= 1
                ans[i] = curr
            else:
                curr = 0
                c = i - 1
                while j < 0:
                    curr += circular[c]
                    c -= 1
                    j += 1
                ans[i] = curr

        return ans
        