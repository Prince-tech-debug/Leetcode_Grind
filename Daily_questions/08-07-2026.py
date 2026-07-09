import bisect
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix sum of digits
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + int(s[i])

        # collect positions of non-zero digits
        nz_pos = []
        nz_digits = []
        for i, ch in enumerate(s):
            if ch != '0':
                nz_pos.append(i)
                nz_digits.append(int(ch))

        # prefix number for non-zero digits
        prefix_num = [0] * (len(nz_digits)+1)
        pow10 = [1] * (len(nz_digits)+1)
        for i, d in enumerate(nz_digits):
            prefix_num[i+1] = (prefix_num[i]*10 + d) % MOD
            pow10[i+1] = (pow10[i]*10) % MOD

        result = []
        for i, j in queries:
            # sum of digits in substring
            segment_sum = prefix_sum[j+1] - prefix_sum[i]

            # find non-zero digits in [i, j]
            L = bisect.bisect_left(nz_pos, i)
            R = bisect.bisect_right(nz_pos, j)

            if L == R:  # no non-zero digits
                new = 0
            else:
                total = prefix_num[R]
                left = prefix_num[L]
                length = R - L
                new = (total - left * pow10[length]) % MOD

            result.append((new * segment_sum) % MOD)

        return result
    

def validate_sum_and_multiply():
    sol = Solution()
    MOD = 10**9 + 7

    # Helper function to compute the expected result via naive brute-force
    def get_expected(s: str, queries: List[List[int]]) -> List[int]:
        expected_results = []
        for i, j in queries:
            substring = s[i:j+1]
            
            # 1. Sum of all digits in the substring
            seg_sum = sum(int(ch) for ch in substring)
            
            # 2. Extract non-zero digits and form a number
            nz_str = "".join([ch for ch in substring if ch != '0'])
            new_num = int(nz_str) if nz_str else 0
            
            # 3. Multiply and modulo
            expected_results.append((new_num * seg_sum) % MOD)
        return expected_results

    # --- Test Case 1: Standard mix of zeros and non-zeros ---
    s1 = "1023"
    queries1 = [[0, 3], [1, 2], [0, 1], [2, 3]]
    # Calculations:
    # [0, 3] -> "1023" -> sum=6, nz_num=123 -> 123 * 6 = 738
    # [1, 2] -> "02"   -> sum=2, nz_num=2   -> 2 * 2 = 4
    # [0, 1] -> "10"   -> sum=1, nz_num=1   -> 1 * 1 = 1
    # [2, 3] -> "23"   -> sum=5, nz_num=23  -> 23 * 5 = 115
    exp1 = get_expected(s1, queries1)
    res1 = sol.sumAndMultiply(s1, queries1)
    assert res1 == exp1, f"Test 1 Failed: Expected {exp1}, got {res1}"

    # --- Test Case 2: String with only zeros ---
    s2 = "0000"
    queries2 = [[0, 3], [1, 2], [0, 0]]
    exp2 = get_expected(s2, queries2)
    res2 = sol.sumAndMultiply(s2, queries2)
    assert res2 == exp2, f"Test 2 Failed: Expected {exp2}, got {res2}"

    # --- Test Case 3: No zeros at all ---
    s3 = "456"
    queries3 = [[0, 2], [1, 2], [0, 0]]
    # [0, 2] -> "456" -> sum=15, nz_num=456 -> 456 * 15 = 6840
    exp3 = get_expected(s3, queries3)
    res3 = sol.sumAndMultiply(s3, queries3)
    assert res3 == exp3, f"Test 3 Failed: Expected {exp3}, got {res3}"

    # --- Test Case 4: Single character queries ---
    s4 = "908"
    queries4 = [[0, 0], [1, 1], [2, 2]]
    exp4 = get_expected(s4, queries4)
    res4 = sol.sumAndMultiply(s4, queries4)
    assert res4 == exp4, f"Test 4 Failed: Expected {exp4}, got {res4}"

    # --- Test Case 5: Large repeat pattern ---
    s5 = "12" * 50  # "121212..." length 100
    queries5 = [[0, 99], [10, 20], [50, 50]]
    exp5 = get_expected(s5, queries5)
    res5 = sol.sumAndMultiply(s5, queries5)
    assert res5 == exp5, f"Test 5 Failed: Expected {exp5}, got {res5}"

    print("All verification tests passed successfully!")


validate_sum_and_multiply()