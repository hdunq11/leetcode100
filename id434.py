class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i-1] == " "):
                count += 1
        return count