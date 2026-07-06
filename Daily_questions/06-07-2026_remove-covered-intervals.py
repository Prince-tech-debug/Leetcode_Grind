from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        result = []
        for i,j in intervals:
            if result:
                if result[-1][0] <= i and result[-1][1] >= j:
                    continue
                elif result[-1][0] == i and result[-1][1] <= j:
                    result[-1] = [i,j]
                else:
                    result.append([i,j])
            else:
               result.append([i,j])
        return len(result) 
                
def validate():
    solve = Solution()
    test_cases = [
        # (intervals, expected_output)
        ([[1,4],[3,6],[2,8]], 2),
        ([[1,4],[2,3]], 1),
        ([[0,10],[5,12]], 2)
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (intervals, expected) in enumerate(test_cases, start=1):
        # Using a deep copy to keep original test list safe across sort calls
        intervals_copy = [item.copy() for item in intervals]
        result = solve.removeCoveredIntervals(intervals_copy)
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()