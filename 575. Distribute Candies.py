class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        # types = dict(Counter(candyType))
        types = set(candyType)

        eatable = len(candyType) / 2

        if len(types) > eatable:
            return eatable
        else:
            return len(types)


        # unique_candies = len(set(candyType))
        # max_candies = len(candyType) // 2
        # return min(unique_candies, max_candies)
        