class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        #practice dict mode
        l = 0
        j = len(jewels)
        stone = dict(Counter(stones))
        count = 0
        while l < j:
            if jewels[l] in stone.keys():
                count += stone[jewels[l]]
            l += 1
        return count

        #easier mode
        # count = 0
        # for i in stones:
        #     if i in jewels:
        #         count+=1
        # return count  