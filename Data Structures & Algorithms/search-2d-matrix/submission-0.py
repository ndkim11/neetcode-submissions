class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            # Target equal : Finished
            if target == matrix[i][0]:
                return True

            # If it belongs to prev row
            elif target < matrix[i][0]:
                i -= 1
                break           

            # Target Bigger : maybe next row / or this row --> keep searching

        for j in range(1,n): #already searched 0th element
            if target == matrix[i][j]:
                return True

        # Haven't found match!
        return False