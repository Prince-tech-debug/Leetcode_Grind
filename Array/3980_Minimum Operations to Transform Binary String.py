

class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        if s1 == '1' and s2 == '0':
            return -1
        count = 0
        s1 = list(s1)
        s2 = list(s2)
        for i in range(len(s1)- 1, 0, -1):
            if s1[i] == s2[i]:
                continue
            if s1[i] == '0' and s2[i] == '1':
                
                count += 1
                s1[i] = '1'
            elif s1[i] == '1' and s2[i] == '0':
                if s1[i-1] == '1':
                    count += 1
                    s1[i] = '0'
                    s1[i-1] = '0'
                else:
                    count +=2
                    s1[i] = '0'
                    s1[i-1] = '0'
        if s1[0] != s2[0]:
            if s1[0] == '0' and s2[0] == '1':
                count += 1
            else:
                count += 2
        
        return count
                
def validate():
    solve = Solution()
    test_cases = [
        # (s1, s2, expected_output)
        ("001", "110", 3),
        ("101", "000", 3),
        ("1", "0", -1),
        ("0", "0", 0)
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (s1, s2, expected) in enumerate(test_cases, start=1):
        result = solve.minOperations(s1, s2)
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()