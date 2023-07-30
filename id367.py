class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = int(num ** 0.5)
        return n ** 2 == num