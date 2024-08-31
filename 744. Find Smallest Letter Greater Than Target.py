class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l = 0
        r = len(letters) - 1
        if ord(letters[-1]) < ord(target):
            return letters[0]
        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) == ord(target):
                l = mid + 1
            elif ord(letters[mid]) > ord(target):
                if ord(letters[mid - 1]) > ord(target):
                    r = mid - 1
                else:
                    return letters[mid]
            elif ord(letters[mid]) < ord(target):
                if ord(letters[mid + 1]) <= ord(target):
                    l = mid + 1
                else:
                    return letters[mid+1]

        return letters[0]
        