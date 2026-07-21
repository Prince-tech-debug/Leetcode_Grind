class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid[0])
        if len(grid) == 1 and m == 1 :
            return grid
        new = []
        for i in grid:
            new += i
        print(new)
        ad = []
        k = k % len(new)
        for i in range(k):
            ad.append(new.pop())
        new = ad[::-1] + new
        n = len(new)
        result = []
        
        for i in range(0,n,m):
            result.append(new[i:i+m])
        return result
