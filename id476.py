class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)[2:]  
        c= ""

        for bit in b:
            if bit == '0':
                c += '1'
            else:
                c += '0'

        return int(c, 2)