class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        hash_map = {0:1}
        island = 1
        result =[]
        for i in range(1,n):
            
            if nums[i] - nums[i-1] > maxDiff:
                island += 1
            hash_map[i] = island
        for i,j in queries:
            result.append(hash_map[i] == hash_map[j])
        return result
def validate_path_existence():
    sol = Solution()
    
    # Test Case 1: Standard case with multiple islands
    # Segments: [1, 3] (diff 2), [10, 12] (diff 2), [20]
    n1 = 5
    nums1 = [1, 3, 10, 12, 20]
    maxDiff1 = 3
    queries1 = [[0, 1], [1, 2], [2, 3], [0, 4]]
    # Expected: 
    # [0,1] -> True (3-1 <= 3)
    # [1,2] -> False (10-3 > 3)
    # [2,3] -> True (12-10 <= 3)
    # [0,4] -> False (Isolated)
    expected1 = [True, False, True, False]
    res1 = sol.pathExistenceQueries(n1, nums1, maxDiff1, queries1)
    assert res1 == expected1, f"Test 1 Failed: Expected {expected1}, got {res1}"
    
    # Test Case 2: Everything is in a single island
    n2 = 4
    nums2 = [1, 2, 3, 4]
    maxDiff2 = 1
    queries2 = [[0, 3], [1, 2]]
    expected2 = [True, True]
    res2 = sol.pathExistenceQueries(n2, nums2, maxDiff2, queries2)
    assert res2 == expected2, f"Test 2 Failed: Expected {expected2}, got {res2}"

    # Test Case 3: Every element is its own isolated island
    n3 = 3
    nums3 = [1, 10, 20]
    maxDiff3 = 5
    queries3 = [[0, 1], [1, 2], [0, 2]]
    expected3 = [False, False, False]
    res3 = sol.pathExistenceQueries(n3, nums3, maxDiff3, queries3)
    assert res3 == expected3, f"Test 3 Failed: Expected {expected3}, got {res3}"

    # Test Case 4: Mirror queries and same-index queries
    n4 = 3
    nums4 = [1, 2, 10]
    maxDiff4 = 2
    queries4 = [[0, 0], [1, 0], [2, 2]]
    expected4 = [True, True, True]
    res4 = sol.pathExistenceQueries(n4, nums4, maxDiff4, queries4)
    assert res4 == expected4, f"Test 4 Failed: Expected {expected4}, got {res4}"

    print("All tests passed successfully!")
validate_path_existence()