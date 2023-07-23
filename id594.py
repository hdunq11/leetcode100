class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        max_length = 0
        for num in num_count:
            if num+1 in num_count:
                max_length = max(max_length, num_count[num]+num_count[num+1])

        return max_length