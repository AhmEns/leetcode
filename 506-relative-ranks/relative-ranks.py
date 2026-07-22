class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_sorted = sorted(score, reverse = True)

        rank_map = {}
        for idx, s in enumerate(score_sorted):
            if idx == 0:
                rank_map[s] = "Gold Medal"
            elif idx == 1:
                rank_map[s] = "Silver Medal"
            elif idx == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(idx + 1)
        
        return [rank_map[s] for s in score]