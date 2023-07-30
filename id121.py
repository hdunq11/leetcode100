class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        min_price = prices[0]
        rs = 0
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                rs = max(rs, prices[i] - min_price)

        return rs