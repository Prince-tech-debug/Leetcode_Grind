from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Approach by seeing 2 Example we comes to the conclusion that if 1 and n belongs to the same connected sequence then the minimum of that sequence is the value we have to return.
        #checking for connected sequence along with the minimum of the sequence
        seen = set()
        MAX = 10**9 - 7
        edges = {}
        for a,b,dist in roads:
            edges.setdefault(a, []).append((b,dist))
            edges.setdefault(b,[]).append((a,dist))
        print(edges)
        mx = []
        def dfs(node,dist,seen,mx,edges):
            if node in seen:
                return MAX
            seen.add(node)
            # mx =dist
            for nxt, distance in edges[node]:
                
                mx.append(distance) 
                dfs(nxt, distance,seen,mx,edges)
            # print(mx)
            return mx if n in seen else []
        return min(dfs(1,float('inf'),seen, mx,edges ))

def validate():
    solve = Solution()
    test_cases = [
        # (n, roads, expected_output)
        (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
        (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2)
    ]
    
    print("Running validation tests...\n" + "-"*30)
    for i, (n, roads, expected) in enumerate(test_cases, start=1):
        result = solve.minScore(n, roads)
        if result == expected:
            print(f"Test {i}: PASSED (Expected: {expected}, Got: {result})")
        else:
            print(f"Test {i}: FAILED ❌ (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    validate()