class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pos=[[] for i in range(3*(10**4)+1)]
        neg=[[] for i in range(3*(10**4)+1)]
        for i in nums:
            if i>=0:
                pos[i].append(0)
            else:
                neg[i].append(0)
        for i in range(0,3*10**4+1):
            if len(pos[i])==1:
                return i
            if len(neg[i])==1:
                return i