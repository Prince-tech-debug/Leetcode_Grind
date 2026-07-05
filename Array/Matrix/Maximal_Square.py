from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
        print(matrix)
        dp = [[0 for i in range(n)] for j in range(m)]
        mx=0
        for i in range(n):
            mx = 1 if matrix[0][i] == 1 else max(mx, 0)
            dp[0][i] = matrix[0][i]
        for i in range(m):
            mx = 1 if matrix[i][0] == 1 else max(mx, 0)
            dp[i][0] = matrix[i][0]
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:
                    a,b,c = dp[i-1][j-1], dp[i-1][j], dp[i][j-1]
                    mn = min(a,b,c)
                    dp[i][j] = mn + 1 
                    mx = max(dp[i][j],mx)
                else:
                    dp[i][j] = matrix[i][j]

        return mx**2

def validate():
    solve = Solution()
    test_cases = [
        # (matrix, expected_output)
        ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
        ([["0","1"],["1","0"]], 1),
        ([["0"]], 0)
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (matrix, expected) in enumerate(test_cases, start=1):
        # Using a deep copy to prevent mutating the original multi-dimensional list across evaluations
        matrix_copy = [row.copy() for row in matrix]
        result = solve.maximalSquare(matrix_copy)
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED ❌ (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()