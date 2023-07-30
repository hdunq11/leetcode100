class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rs=0
        while n:
            rs+=n&1
            n>>=1
        return rs