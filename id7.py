class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            rs = int(str(x)[::-1])
        else:
            rs = -1 * int(str(-1 * x)[::-1])
        if rs < -2**31 or rs > 2**31 - 1:
            return 0
        else:
            return rs