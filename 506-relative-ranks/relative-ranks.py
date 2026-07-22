class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_sorted = sorted(score, reverse = True)
        ans = []

        for i in score:
            rank = score_sorted.index(i)
            if i == score_sorted[0]:
                ans.append("Gold Medal")
            elif i == score_sorted[1]:
                ans.append("Silver Medal")
            elif i == score_sorted[2]:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank + 1))
        
        return ans