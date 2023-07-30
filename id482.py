class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        f = len(s) % k
        result = []

        if f != 0:
            result.append(s[:f])

        for i in range(f, len(s), k):
            result.append(s[i:i+k])

        return "-".join(result)