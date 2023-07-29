class Solution(object):
    def countBinarySubstrings(self, s):
        count = 0
        n = len(s)
        substrings = []
        
        for i in range(n):
            zeros = ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    zeros += 1
                else:
                    ones += 1
                
                if zeros == ones and (j == n-1 or s[j+1] != s[j]):
                    substr = s[i:j+1]
                    if substr not in substrings:
                        substrings.append(substr)
                        count += 1
            
        return count