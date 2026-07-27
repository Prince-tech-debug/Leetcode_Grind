class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = float('-inf')
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                n = max(n, (nums[i] - 1) * (nums[j] - 1))
        return n
                