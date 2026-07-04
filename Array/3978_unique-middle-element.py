

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = nums[len(nums)//2 ]
        count = 0
        for i in nums:
            if i == mid:
                count += 1
        return True if count == 1 else False

def validate():
    solve = Solution()
    test_cases = [
        # (nums, expected_output)
        ([1, 2, 3, 4, 5], True),     # Mid is 3, appears once
        ([1, 3, 3, 4, 5], False),    # Mid is 3, appears twice
        ([1, 2, 2, 2], False),       # Mid is 2, appears three times
        ([1], True)                  # Single element is always unique
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = solve.isMiddleElementUnique(nums)
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED ❌ (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()