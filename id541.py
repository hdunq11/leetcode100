class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        n = len(s)
        for i in range(0, n, 2*k):
            j = min(i + k - 1, n - 1)
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)