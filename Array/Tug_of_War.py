#
# Tug Of War Captain

#     You are given N kids, where the i-th kid has a strength of s[i].
#     The kids will line up to grab a long rope one at a time in an order that you choose.
#     When a kid grabs the rope, they must join the side (left or right) that currently has the strictly smaller total strength.
#     If the two sides currently have equal total strength (including at the very beginning when both sides have 0 strength),
#     the kid can choose to join either side.

#     Before the process begins, you must appoint exactly one kid as the captain.
#     The captain’s strength is doubled for the entire process.

#     Your goal is to choose the captain and the order in which the kids join the rope
#     to minimize the final absolute difference between the total strength of the left side and the right side (the final imbalance).

#     Find the minimum possible final imbalance.
# 
class Solution():
    def divide(self, n:int, total:int, nums: list):
        
        for i in nums:
            if total == 0:
                total += i
            elif total > 0 :
                total -= i
            else :
                total += i
        return abs(total)
    
            
        
    
if __name__ == "__main__":
    n = int(input())
    nums = [int(input()) for i in range(n)]
    nums.sort(reverse = True)
    solve = Solution()
    ans = float('inf')
    for i in range(n):
        nums[i] = nums[i] *2
        # print(nums)
        ans = min(ans, solve.divide(n, 0, nums))
        # print(solve.divide(n, 0, nums))
        nums[i] = nums[i] /2
        
        # print(nums)
   
    print(ans)