# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)
        for key, cnt in count.items():
            bucket[cnt].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) != k:
                if bucket[i] != []:
                    res.extend(bucket[i])
            else:
                return res
        return res
