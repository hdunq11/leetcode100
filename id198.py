class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        rs = 0
        prev_max = 0

        for i in range(n):
            curr_max = max(prev_max + nums[i], rs)
            prev_max = rs
            rs = curr_max

        return rs