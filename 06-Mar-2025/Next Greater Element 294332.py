# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        st = []
        map_nums1 = {num: index for index, num in enumerate(nums1)} 
        for i in range(len(nums2)):
            
            while st and nums2[st[-1]] < nums2[i]:
                top = st.pop()
                refer = nums2[top]

                if refer in map_nums1:
                    ans[map_nums1[refer]] = nums2[i]
        
            st.append(i)

        return ans

        
