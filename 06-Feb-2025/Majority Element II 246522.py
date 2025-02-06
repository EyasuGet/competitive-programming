# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

count = int(len(nums) / 3)

ans = []
freq = Counter(nums)

for key,value in freq.items():
        if value > count:
            ans.append(key)
return ans