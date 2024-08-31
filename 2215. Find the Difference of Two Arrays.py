class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = [[],[]]
        nums1 =set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i not in nums2:
                answer[0].append(i)

        for i in nums2:
            if i not in nums1:
                answer[1].append(i)
        return answer
                
        