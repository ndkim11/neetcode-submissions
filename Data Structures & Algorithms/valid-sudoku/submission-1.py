from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True
        for i in range(9):
            # print(board[i][:])
            temp = Counter(board[i])
            # print(temp)
            if not self.countNums(temp):
                ans = False
                return ans


        for i in range(9):
            column_elements = [board[row][i] for row in range(9)]
            temp = Counter(column_elements)
            # print(temp)
            if not self.countNums(temp):
                ans = False
                return ans

        for i in range(0,9,3):
            for j in range(0,9,3):
                temp = Counter([board[r][c] for r in range(i,i+3) for c in range(j,j+3)])
                if not self.countNums(temp):
                    ans = False
                    return ans

        return ans

    def countNums(self, count):
        for key,ele in count.items():
            if ele>1 and not key=='.':
                return False

        return True