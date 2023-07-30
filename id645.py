class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []

        rs = []
        n = len(nums)
        s = sum(nums)
        num = sum(set(nums))
        dup = s - num
        miss = n * (n + 1) // 2 - num
        rs.append(dup)
        rs.append(miss)
        return rs