class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        Mod = 10 ** 9 + 7
        dp = [[1]* (n+2) for i in range(m + 2)]
        for i in range(n+2):
            dp[0][i] = 0
            dp[-1][i] = 0
        for i in range(m+2):
            dp[i][0] = 0
            dp[i][-1] = 0
        print(dp)
        startRow +=1
        startColumn += 1
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        @lru_cache(None)
        def check(x,y,n):
            if n > maxMove:
                return 0
            if dp[x][y] == 0:
                return 1
            
            total = 0
            for i,j in directions:
                nx,ny = x+i , y+j
                total += check(nx,ny,n+1)
            return total
        return check(startRow,startColumn, 0) % Mod
