# Last updated: 30/07/2026, 15:14:39
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6
7        n=len(matrix)
8
9        for i in range(n):
10
11            for j in range(i, n):
12
13                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
14        
15        for row in matrix:
16
17            row.reverse()
18        
19        return matrix
20        