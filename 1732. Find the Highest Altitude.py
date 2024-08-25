class Solution(object):
    def largestAltitude(self, gain):
        if len(gain) == 2:
            return gain[0] + gain[1]
        answer = [0]
        for i in range(len(gain)):
            net = answer[i] + gain[i]
            answer.append(net)
        return max(answer)

        # altitude = 0
        # max = 0
        # for i in gain:
        #     altitude += i:
        #     if altitude > max:
        #         max = altitude
        # return max
        