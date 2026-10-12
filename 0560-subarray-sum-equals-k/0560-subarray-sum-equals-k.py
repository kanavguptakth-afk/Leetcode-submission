class Solution:
    def subarraySum(self, nums,k):
        prefix={0:1}
        total=0
        count=0

        for num in nums:
            total+=num
            count+=prefix.get(total-k,0)
            prefix[total]=prefix.get(total,0)+1

        return count      
        