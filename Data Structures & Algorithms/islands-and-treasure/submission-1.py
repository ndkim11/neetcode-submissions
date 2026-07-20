class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # IMPORTANT
        if not grid:
            return

        n,m = len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                # if treasure
                if grid[i][j]==0: 
                    q.append((i,j))

        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r, c = q.popleft()

            for dr,dc in direction:
                nr, nc = r+dr, c+dc

                if nr<0 or nr>= n or nc<0 or nc >= m:
                    continue

                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))

