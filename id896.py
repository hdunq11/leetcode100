class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        
        is_increasing = None
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                if is_increasing is None:
                    is_increasing = True
                elif not is_increasing:
                    return False
            elif nums[i] > nums[i+1]:
                if is_increasing is None:
                    is_increasing = False
                elif is_increasing:
                    return False
        
        return True