class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return_value = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    n = 4

                    if j > 0 and grid[i][j - 1] == 1:
                        n -= 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        n -= 1
                    if i > 0 and grid[i - 1][j] == 1:
                        n -= 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        n -= 1
                   
                    return_value += n
        return return_value