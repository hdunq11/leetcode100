class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mlen = 0
        count = 0
        for num in nums:
            count = (count + 1) if (num & 1) else 0
            mlen = max(mlen, count)
        return mlen