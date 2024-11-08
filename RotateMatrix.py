from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Take transpose
        n = len(matrix)
        for row in range(n):
            for col in range(n - row - 1):
                tmp_var = matrix[row][col]
                matrix[row][col] = matrix[n - col - 1][n - row - 1]
                matrix[n - col - 1][n - row - 1] = tmp_var

        # Flip the matrix
        for row in range(n // 2):
            for col in range(n):
                print('flip')
                print(f'row: {row}, col: {col}')
                tmp_var = matrix[row][col]
                matrix[row][col] = matrix[n - row - 1][col]
                matrix[n - row - 1][col] = tmp_var