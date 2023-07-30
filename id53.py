class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rs=nums[0]
        sum=nums[0]
        for i in range(1, len(nums)):
            sum=max(nums[i], sum+nums[i])
            rs=max(rs, sum)
        return rs
      