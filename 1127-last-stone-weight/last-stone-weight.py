class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            top_two = sorted(stones, reverse=True)[:2]
            stones.remove(top_two[1])
            stones.remove(top_two[0])

            if top_two[0] != top_two[1]:
                stones.append(top_two[0] - top_two[1])

        return stones[0] if stones else 0