class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0, 0]
        for i in moves:
            if i == "U":
                pos[1] += 1
            elif i == "D":
                pos[1] -= 1
            elif i == "R":
                pos[0] += 1
            else:
                pos[0] -= 1
        return pos[0] == 0 and pos[1] == 0