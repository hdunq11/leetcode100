class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rs = nums[0]
        count = 1
        for num in nums[1:]:
            if num == rs:
                count += 1
            else:
                count -= 1
                if count == 0:
                    rs = num
                    count = 1
        return rs