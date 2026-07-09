class Solution:
    def sumAndMultiply(self, n: int) -> int:
        result = 0
        count = 0
        suma = 0
        while n > 0:
            mode = n % 10
            if mode != 0:
                result += (10**count) * mode
                suma += mode
                count += 1
            n//=10
        return result * suma
def validate_sum_and_multiply_int():
    sol = Solution()

    # Simple reference function for comparison
    def get_expected(n: int) -> int:
        if n == 0:
            return 0
        # Filter out '0' characters from the string representation
        digits = [int(ch) for ch in str(n) if ch != '0']
        if not digits:
            return 0
        
        # Reconstruct the number and calculate the sum
        nz_num = int("".join(str(d) for d in digits))
        total_sum = sum(digits)
        return nz_num * total_sum

    # --- Test Case 1: Standard number with no zeros ---
    n1 = 123
    # Digits: 1, 2, 3 -> New Number = 123, Sum = 6 -> 123 * 6 = 738
    assert sol.sumAndMultiply(n1) == get_expected(n1), f"Failed for {n1}"

    # --- Test Case 2: Number with trailing and embedded zeros ---
    n2 = 102030
    # Zeroes dropped -> New Number = 123, Sum = 6 -> 123 * 6 = 738
    assert sol.sumAndMultiply(n2) == get_expected(n2), f"Failed for {n2}"

    # --- Test Case 3: Single non-zero digit ---
    n3 = 7
    # New Number = 7, Sum = 7 -> 7 * 7 = 49
    assert sol.sumAndMultiply(n3) == get_expected(n3), f"Failed for {n3}"

    # --- Test Case 4: Power of 10 ---
    n4 = 10000
    # Zeroes dropped -> New Number = 1, Sum = 1 -> 1 * 1 = 1
    assert sol.sumAndMultiply(n4) == get_expected(n4), f"Failed for {n4}"

    # --- Test Case 5: Large input sequence ---
    test_inputs = [504, 999, 1002, 450607]
    for n in test_inputs:
        res = sol.sumAndMultiply(n)
        exp = get_expected(n)
        assert res == exp, f"Failed for {n}: Expected {exp}, got {res}"

    print("All integer validation tests passed successfully!")

validate_sum_and_multiply_int()