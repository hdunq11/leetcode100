class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        rs = float('-inf')
        rs = max(rs, nums[n-1] * nums[n-2] * nums[n-3])
        rs = max(rs, nums[0] * nums[1] * nums[n-1])
        return rs