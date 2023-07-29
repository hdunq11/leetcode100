class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        rs = {}
        for i in range(1, len(numbers)+1):
            c = target - numbers[i-1]
            if c in rs:
                return [rs[c]+1, i]
            rs[numbers[i-1]] = i-1