class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        for num in nums:
            if num not in s:
                s.append(num)
        nums[:] = s
        return len(nums)