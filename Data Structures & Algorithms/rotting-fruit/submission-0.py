from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1 <= grid.length, grid[i].length <= 10
        # no rotten possible
        n,m = len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j,0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_time = 0
        while q:
            r, c, t = q.popleft()
            for dr,dc in directions:
                nr, nc = r+dr,c+dc
                if nr >= n or nr < 0 or nc >= m or nc < 0:
                    continue

                # fresh banana
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2 # change to rotten banana
                    q.append([nr,nc,t+1])
                    max_time = max(max_time,t+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1

        return max_time
                