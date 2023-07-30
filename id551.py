class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0

        for char in s:
            if char == 'A':
                a += 1
                l = 0
            elif char == 'L':
                l += 1
                if l == 3:
                    return False
            else:  
                l = 0

        return a < 2 and l < 3