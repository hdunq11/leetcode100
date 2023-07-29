class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        s = sorted(score, reverse=True)
        rank = 1
        rs = [""] * n
        for i in range(n):
            if s.index(score[i]) == 0:
                rs[i] = "Gold Medal"
            elif s.index(score[i]) == 1:
                rs[i] = "Silver Medal"
            elif s.index(score[i]) == 2:
                rs[i] = "Bronze Medal"
            else:
                rs[i] = str(s.index(score[i]) + 1)
            rank += 1
        return rs