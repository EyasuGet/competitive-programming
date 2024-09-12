class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        x = 0

        for i in operations:
            if i.__contains__("-"): #or we can use if "-" in i
                x -= 1
            else:
                x += 1
        return x
        