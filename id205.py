class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        cmap = {}
        for i in range(len(s)):
            if s[i] not in cmap:
                if t[i] in cmap.values():
                    return False
                cmap[s[i]] = t[i]
            else:
                if cmap[s[i]] != t[i]:
                    return False
        
        return True