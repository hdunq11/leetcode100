class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left <= right:
            k = (left + right) // 2
            coins = (k * (k + 1)) // 2
            if coins <= n:
                left = k + 1
            else:
                right = k - 1
        return left - 1