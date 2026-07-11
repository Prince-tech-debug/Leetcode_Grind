from collections import deque
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        paths = {}
        for i,j in edges:
            paths.setdefault(i,[]).append(j)
            paths.setdefault(j,[]).append(i)
        
        seen = set()
        graphs = []
        def bfs(node,seen, paths):
            edges = 0
            graph = [node]
            seen.add(node)
            q = deque([node])
            while q:
                node = q.popleft()
                path = paths.get(node,[])
                edges += len(path)
                for i in path:
                    if i not in seen:
                        seen.add(i)
                        q.append(i)
                        graph.append(i)
            graphs.append((len(graph), edges/2))
        
        for i in range(n):
            if i not in seen:
                bfs(i, seen,paths)
        
        count =0
        for i,j in graphs:
            com = i * (i-1)/2
            
            if j == com:
                count +=1    
        return count    
def validate_count_complete():
    sol = Solution()
    test_cases = [
        # Format: (n, edges, expected_output)
        (6, [[0,1],[0,2],[1,2],[3,4]], 3),   # {0,1,2} is complete, {3,4} is complete, {5} is complete → total 3
        (4, [[0,1],[1,2],[2,3]], 0),         # chain of 4 nodes, not complete
        (3, [[0,1],[1,2],[0,2]], 1),         # triangle is complete
        (5, [], 5),                          # all isolated nodes are trivially complete
        (5, [[0,1],[1,2],[2,0],[3,4]], 2),   # triangle + edge + isolated node → 3 complete
    ]
    
    for i, (n, edges, expected) in enumerate(test_cases, 1):
        result = sol.countCompleteComponents(n, edges)
        print(f"Test {i}: result={result}, expected={expected}, pass={result == expected}")
validate_count_complete()