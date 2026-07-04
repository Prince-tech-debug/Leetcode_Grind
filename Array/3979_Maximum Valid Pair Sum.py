

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        
        if len(nums) < k + 1:
            return  -1
        mx = float('-inf')
        mx_seen = float('-inf')
        for j in range(k, len(nums)):
            mx_seen = max(mx_seen , nums[j - k])
            mx = max(mx, mx_seen + nums[j])
        return mx
                
def validate():
    solve = Solution()
    test_cases = [
        # (nums, k, expected_output)
        ([1, 2, 3, 4, 5], 2, 8),     # Pairs with index diff >= 2: (3+5)=8, (2+5)=7, etc.
        ([5, 1, 1, 5], 3, 10),       # Only indices 0 and 3 are apart by >= 3: 5 + 5 = 10
        ([1, 2], 2, -1)              # Length < k + 1, returns -1
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (nums, k, expected) in enumerate(test_cases, start=1):
        result = solve.maxValidPairSum(nums, k)
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED ❌ (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()