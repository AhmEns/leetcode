class Solution(object):
    def calPoints(self, operations):
        stack = []
        totalScore = 0
        for op in operations:
            if op == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)
                totalScore += val
            elif op == 'D':
                val = 2 * stack[-1]
                stack.append(val)
                totalScore += val
            elif op == 'C':
                totalScore -= stack.pop()
            else:
                val = int(op)
                stack.append(val)
                totalScore += val
        return totalScore