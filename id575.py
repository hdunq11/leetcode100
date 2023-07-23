class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType) // 2
        rs = set(candyType)
        return min(len(rs), n)