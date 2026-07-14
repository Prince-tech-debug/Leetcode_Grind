from math import gcd
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        maxVal = max(nums)

        MOD = 10**9 +7
        # dp[i][gA][gB] = number of ways from index i with gcdA=gA, gcdB=gB
        dp = [[[0]*(maxVal+1) for _ in range(maxVal+1)] for _ in range(n+1)]

        # Base case: at the end
        for gA in range(1, maxVal+1):
            for gB in range(1, maxVal+1):
                if gA == gB:
                    dp[n][gA][gB] = 1

        
        for i in range(n-1, -1, -1):
            x = nums[i]
            for gA in range(maxVal+1):
                for gB in range(maxVal+1):
                    val = dp[i+1][gA][gB]  # skip
                    newA = x if gA == 0 else gcd(gA, x)
                    newB = x if gB == 0 else gcd(gB, x)
                    val += dp[i+1][newA][gB]
            # put x in B
                    val += dp[i+1][gA][newB]
                    dp[i][gA][gB] = val % MOD

        return dp[0][0][0]



        # Simple memoization
        # def total(i, curr1,curr2,memo):
        #     if (i,curr1,curr2) in memo:
        #         return memo[(i,curr1,curr2)]
        #     if i == len(nums):
        #         return 1 if curr1 > 0 and curr2 == curr1 else 0
        #     x = nums[i]
        #     memo[(i+1,curr1,curr2)] = total(i + 1, curr1, curr2,memo)
        #     skip = memo[(i+1,curr1,curr2)]
        #     memo[(i + 1, gcd(curr1,x) if curr1 else x,curr2)] = total(i + 1, gcd(curr1,x) if curr1 else x,curr2,memo)
        #     take1 = memo[(i + 1, gcd(curr1,x) if curr1 else x,curr2)]
        #     memo[(i + 1, curr1, gcd(curr2,x) if curr2 else x)] = total(i + 1, curr1, gcd(curr2,x) if curr2 else x,memo)
        #     take2 = memo[i + 1, curr1, gcd(curr2,x) if curr2 else x]
        #     return (take1 + take2 + skip)%(10**9+7)
        # return total(0,0,0, {})
def validate():
    solve = Solution()
    test_cases = [
        # (nums, expected_output)
        ([1, 2, 3,4], 10),
        ([10, 20, 30], 2),
        ([1,1,1,1], 50)
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (nums, expected) in enumerate(test_cases, start=1):
        try:
            result = solve.subsequencePairCount(nums)
            if result == expected:
                print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
            else:
                print(f"Test {i}: FAILED (Expected: {expected}, Got: {result})")
        except Exception as e:
            print(f"Test {i}: FAILED due to error: {str(e)}")

if __name__ == '__main__':
    validate()