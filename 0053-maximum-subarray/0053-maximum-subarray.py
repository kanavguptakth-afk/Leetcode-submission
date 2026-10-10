class Solution:
    def maxSubArray(self, nums):
        curr = nums[0]
        maximum = nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i],curr + nums[i])
            maximum = max(maximum, curr)
        return maximum
        
        