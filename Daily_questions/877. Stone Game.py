
class Solution:
    @lru_cache(None)
    def recur(self,i,j,s):
        if i == j:
            return self.nums[i]
        if s == 0:
            left = self.nums[i] + self.recur(i + 1,j , 1)
            right = self.nums[j] + self.recur(i, j - 1, 1)
            return max(left , right)
        else:
            left = self.recur(i + 1, j , 0)
            right = self.recur(i , j - 1, 0)
            return min(left ,right) 

    def stoneGame(self, piles: List[int]) -> bool:
        self.nums = piles
        self.n = len(self.nums)
        return self.recur(0, (self.n - 1), 0) > sum(piles) // 2