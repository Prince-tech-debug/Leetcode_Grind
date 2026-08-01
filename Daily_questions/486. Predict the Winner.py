class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        @lru_cache(None)
        def recur(i,j, s):
            if i == j:
                return nums[i]
            if s == 0:
                left = nums[i] + recur(i + 1, j, 1)
                right = nums[j] + recur(i,j - 1, 1) 
                return max(left, right)
            else:
                left = recur(i + 1, j, 0)
                right = recur(i, j - 1, 0)
                return min(left, right)
        return recur(0, len(nums) - 1, 0) >= total /2
                

            



        
            
           
            
            
        #     return n
        # return recur(0,len(nums) - 1, 0,0)