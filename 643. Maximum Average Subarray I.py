
def findMaxAverage( nums, k):
    currentSum = float(0)
    max_average = float("-inf")
    for i in range(len(nums)):
        currentSum += nums[i]
        if (i >= k - 1):
            max_average = max(currentSum/k, max_average)
            print(max_average)
            currentSum -= nums[i - (k - 1)]
    return max_average

