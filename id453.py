from typing import List

class Solution(object):
    def minMoves(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        k = min(nums)
        rs = sum(num - k for num in nums)
        return rs