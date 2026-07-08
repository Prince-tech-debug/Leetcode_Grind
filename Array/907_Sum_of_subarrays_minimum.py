class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [] 
        res = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                prev = stack[-1]
                res[i] = res[prev] + (i - prev) * arr[i]
            else:
                res[i] = (i+1)* arr[i]

            stack.append(i)
        
        return sum(res) % (10**9+7)
def validate_sumSubarrayMins():
    sol = Solution()

    # Test cases: (input, expected_output)
    tests = [
        ([3, 1, 2, 4], 17),   # Example from LeetCode
        ([11, 81, 94, 43, 3], 444),
        ([1], 1),
        ([2, 9, 7, 8, 3, 4, 6, 1], 117),
        ([71, 55, 82, 55], 593)
    ]

    all_passed = True
    for arr, expected in tests:
        result = sol.sumSubarrayMins(arr)
        if result != expected:
            print(f" Failed for {arr}: got {result}, expected {expected}")
            all_passed = False
        else:
            print(f" Passed for {arr}: {result}")

    if all_passed:
        print("\n All test cases passed!")
    else:
        print("\n Some test cases failed.")

validate_sumSubarrayMins()
            