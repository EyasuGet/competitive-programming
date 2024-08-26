class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return nums
            
        answer = []
        left = 0
        curr = 0

        while left < len(nums)-1:
            if ((nums[left] + 1) == nums[left+1]):
                left += 1
            elif curr - left == 0:
                answer.append(str(nums[curr]))
                left += 1
                curr += 1
            else:
                answer.append(str(nums[curr]) + "->" + str(nums[left]))
                left += 1
                curr = left
        
        if curr == left:
            answer.append(str(nums[curr]))
        else:
            answer.append(str(nums[curr]) + "->" + str(nums[left]))
        
        return answer       
            
          
        