class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            m = self.countAndSay(n-1)
            rs = ""
            count = 1
            for i in range(len(m)):
                if i < len(m)-1 and m[i] == m[i+1]:
                    count += 1
                else:
                    rs += str(count) + m[i]
                    count = 1
            return rs