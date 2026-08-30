class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set() #bot lef --> top ri
        neg_diag = set() #top lef --> bot ri

        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r: int):
            if r==n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue

                # place queen
                cols.add(c)
                pos_diag.add(c+r)
                neg_diag.add(r-c)
                board[r][c] = 'Q'

                #recursive call to next row
                backtrack(r+1)

                # place queen
                cols.remove(c)
                pos_diag.remove(c+r)
                neg_diag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return res