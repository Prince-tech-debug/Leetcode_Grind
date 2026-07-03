
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        health -= grid[0][0]
        if health < 1:
            return False
            
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True

        seen = set()
        q = [(health, 0, 0)]
        seen.add((health, 0, 0))
        
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            health, i, j = q.pop(0)
            
            for x, y in direction:
                new_x, new_y = i + x, j + y
                
                if new_x > m - 1 or new_x < 0 or new_y > n - 1 or new_y < 0:
                    continue

                value = grid[new_x][new_y] 
                next_health = health - 1 if value == 1 else health
                
                if (next_health, new_x, new_y) in seen:
                    continue
                
                if next_health >= 1:
                    if new_x == m - 1 and new_y == n - 1:
                        return True
                        
                    q.append((next_health, new_x, new_y))
                    seen.add((next_health, new_x, new_y))
            
        return False
    
def validate():
    solve = Solution()
    test = [
        ([[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]],3,False),
        ([[1,1,1],[1,0,1],[1,1,1]],5, True),
        ([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],1,True)
    ]
    for grid, health, output in test:
        result = solve.findSafeWalk(grid, health)
        if result == output:
            print(f"PASSED result = {output}")
        else:
            print(f"FAILED result = {result}")

if __name__ == '__main__':
    validate()