class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        max_area = 0

        def dfs(i,j):
            if i>=n or i<0 or j>=m or j<0:
                return 0

            # searching neighbors and find 0(water)
            if grid[i][j] == 0:
                return 0

            area = 1
            grid[i][j] = 0
            area += dfs(i+1,j)
            area += dfs(i-1,j)
            area += dfs(i,j-1)
            area += dfs(i,j+1)
            
            return area

        for i in range(n):
            for j in range(m):
                # scanning through and incounter 0(water)
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))

        return max_area