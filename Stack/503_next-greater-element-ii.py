from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        new = nums[::-1] + nums[::-1]
        n = len(new)
        res_nums = [-1 for i in range(n)]
        
        for i in range(n):
            if stack and new[i] < new[stack[-1]]:
                res_nums[i] = new[stack[-1]]
                stack.append(i)
            else:
                while stack and new[i] >= new[stack[-1]]:
                    stack.pop()
                if stack != []:
                    res_nums[i] = new[stack[-1]]
                stack.append(i)
                        
        res_nums = res_nums[n : n//2-1: -1]
        return res_nums

def validate():
    solve = Solution()
    test_cases = [
        # (nums, expected_output)
        ([1, 2, 1], [2, -1, 2]),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
        ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5])
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (nums, expected) in enumerate(test_cases, start=1):
        # Pass a shallow copy to prevent internal modifications from affecting print statements
        result = solve.nextGreaterElements(nums.copy())
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED ❌ (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()