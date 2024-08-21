class Solution(object):
    def checkIfExist(self, arr):
        seen = {}
        for i in range(len(arr)):
            if 2*arr[i] in seen or (arr[i] % 2 == 0 and arr[i] // 2 in seen):
                return True
            else:
                seen[arr[i]] = i
        return False
