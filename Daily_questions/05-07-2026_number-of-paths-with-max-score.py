from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7

        dp_score = [[-float('inf')] * n for _ in range(n)]
        dp_paths = [[0] * n for _ in range(n)]
        dp_score[n-1][n-1] = 0
        dp_paths[n-1][n-1] = 1

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if board[i][j] == 'X':
                    continue
                if board[i][j] == 'S':
                    continue

                candidates = [(i+1, j), (i, j+1), (i+1, j+1)]
                max_score = -float('inf')
                path_count = 0

                for x, y in candidates:
                    if x < n and y < n and dp_paths[x][y] > 0:
                        if dp_score[x][y] > max_score:
                            max_score = dp_score[x][y]
                            path_count = dp_paths[x][y]
                        elif dp_score[x][y] == max_score:
                            path_count = (path_count + dp_paths[x][y]) % MOD

                if path_count > 0:
                    cell_value = 0 if board[i][j] in "SE" else int(board[i][j])
                    dp_score[i][j] = cell_value + max_score
                    dp_paths[i][j] = path_count

        return [dp_score[0][0], dp_paths[0][0]] if dp_paths[0][0] > 0 else [0, 0]

def validate():
    solve = Solution()
    test_cases = [
        # (board, expected_output)
        (["E23","2X2","12S"], [7, 1]),
        (["E12","1X1","21S"], [4, 2]),
        (["E11","1X1","11S"], [0, 0])
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (board, expected) in enumerate(test_cases, start=1):
        result = solve.pathsWithMaxScore(board)
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()