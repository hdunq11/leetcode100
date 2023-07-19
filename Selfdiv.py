class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            if self.isSelfDividing(num):
                res.append(num)
        return res
    
    def isSelfDividing(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True
left = int(input("left ="))
right = int(input("right= "))

s = Solution()
result = s.selfDividingNumbers(left, right)
print( result)