class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = list(s)
        t1 = list(t)
        s1.sort()
        t1.sort()
        s2 = ''.join(s1)
        t2 = ''.join(t1)
        if s1 == t1:
            return True
        else:
            return False
# s1, t1 là s và t chuyển thành list
