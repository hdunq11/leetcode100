class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = []
        count = 1
        for i in range(1, len(chars) + 1):
            if i == len(chars) or chars[i] != chars[i - 1]:
                res.append(chars[i - 1])
                if count > 1:
                    res.extend(list(str(count)))
                count = 1
            else:
                count += 1
        
        chars[:] = res
        return len(chars)