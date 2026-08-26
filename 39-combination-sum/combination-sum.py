class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return [[]]

        candidates.sort()
        result = []

        for i, num in enumerate(candidates):
            if num > target:
                break

            sub_combinations = self.combinationSum(candidates[i:], target - num)

            for comb in sub_combinations:
                result.append([num] + comb)

        return result