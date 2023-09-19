from typing import List
# 单调栈（递增）
# 对于矩阵中的每个位置i,j，计算该位置往左的长条有多长，记为left_length
# 对于每一列，变成了84题，使用单调栈计算出最大的面积
# 按每列循环求解

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        left_length = [[0] * len(matrix[0]) for _ in range(len(matrix) + 2)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    left_length[i+1][j] = 1 if j == 0 else left_length[i+1][j - 1] + 1
        area = 0
        for j in range(len(matrix[0])):
            stack = [0]
            for i in range(1, len(matrix) + 2):
                while left_length[i][j] < left_length[stack[-1]][j]:
                    area = max(area, left_length[stack.pop()][j] * (i - stack[-1] - 1))
                stack.append(i)
        return area


print(Solution().maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
