class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        islands = 0

        def dfs(i,j):
            # it is 0 --> do not visit
            if i>=n or i<0 or j>=m or j<0:
                return

            if grid[i][j] == '0':
                return

            grid[i][j] = '0' # mark as visited
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    islands += 1
                    dfs(i,j)

        return islands