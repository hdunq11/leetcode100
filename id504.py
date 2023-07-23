class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        n = abs(num)
        while n >= 7:
            s = str(n % 7) + s
            n //= 7
        s = str(n) + s
        return '-' + s if num < 0 else s