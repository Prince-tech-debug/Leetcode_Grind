from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        n, m = len(grid), len(grid[0])
              
        seen = set()
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i,j))
                    seen.add((i,j))
        # print(q)
        
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            i,j = q.popleft()
            for x,y in direction:
                new_x , new_y = i + x, j+ y
                if new_x > n-1 or new_x < 0 or new_y > m-1 or new_y < 0 or (new_x , new_y) in seen:
                    continue
                if grid[new_x][new_y] != 0:
                    grid[new_x][new_y] = min(grid[new_x][new_y], grid[i][j] + 1)
                else:
                    grid[new_x][new_y] = grid[i][j] + 1                
                q.append((new_x , new_y))
                seen.add((new_x , new_y))
        # print(grid)
        def possible(mid,grid, directions) -> bool:
            seen = set()
            q = deque([(0,0)])
            while q:
                i,j = q.popleft()
                for x,y in directions:
                    new_x , new_y = i + x, j+ y
                    if new_x == n-1 and new_y == m-1 and grid[new_x][new_y] >= mid:
                        return True
                    if new_x > n-1 or new_x < 0 or new_y > m-1 or new_y < 0 or (new_x , new_y) in seen:
                        continue
                    if grid[new_x][new_y] >= mid:
                        q.append((new_x,new_y))
                        seen.add((new_x, new_y))
            return False
        left, right = 0, min(grid[0][0],grid[-1][-1])
        mx = 0
        while left <= right:
            mid = left + (right - left)//2
            if possible(mid, grid, direction):
                left = mid + 1
                mx = max(mx, mid)
            else:
                right = mid - 1
        return mx -1

def validate():
    solve = Solution()
    test=[
        ([[0,0,1],[0,0,0],[0,0,0]],2),
        ([[1,0,0],[0,0,0],[0,0,1]], 0),
        ([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]], 2),
        ([[0,1,1],[0,1,1],[1,1,0]], 0)
    ]
    for input, output in test:
        print('PASSED') if solve.maximumSafenessFactor(input) == output else print('FAILED')
validate()
            
        
# What i did was from every '1' in grid i calculate the mahattan distance of every other 
# grid and stored the minimun except if the cell is 0 then store directly. and then applied
# simple binary search on possible values which can be the answers.