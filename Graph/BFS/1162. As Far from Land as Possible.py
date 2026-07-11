from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf') for i in range(n)] for i in range(n)]
        q= deque([])
        seen = set()
        for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        q.append((i,j))
                        seen.add((i,j))
                        dp[i][j] = 0
        if q:
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            
            mx = 0
            dist = -1 # if you are currently on land you are currently -1 away when you just enter water you are 0 away
            while q:
                for _ in range(len(q)):
                    node_x, node_y = q.popleft()
                    for x,y in directions:
                        new_x, new_y = node_x + x ,node_y + y
                        if new_x < 0 or new_x > n-1 or new_y < 0 or new_y > n-1 or (new_x,new_y) in seen:
                            continue
                        if dp[new_x][new_y] > dp[node_x][node_y] + 1:
                            dp[new_x][new_y] = dp[node_x][node_y] + 1
                            q.append((new_x,new_y))
                            seen.add((new_x,new_y)) 
                        else:
                            continue
                dist += 1
        else:
            return -1
            
        
        return dist if dist != 0 else -1
        

def validate():
    sol = Solution()
    test_cases = [
        # Format: (grid, expected_output)
        ([[1,0,0],[0,0,0],[0,0,1]], 2),   # water cell farthest from land is distance 2
        ([[1,0,1],[0,0,0],[1,0,1]], 2),   # center water cell is 1 away
        ([[1,1,1],[1,1,1],[1,1,1]], -1),  # all land → -1
        ([[0,0,0],[0,0,0],[0,0,0]], -1),  # all water → -1
        ([[0,1],[1,0]], 1),               # each water cell is 1 away
    ]
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = sol.maxDistance([row[:] for row in grid])  # copy grid to avoid mutation
        print(f"Test {i}: result={result}, expected={expected}, pass={result == expected}")
validate()
