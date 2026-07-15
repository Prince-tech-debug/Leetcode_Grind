class Solution:
    def gc(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def gcdOfOddEvenSums(self, n: int) -> int:
    
        return self.gc(n*n,n*(n+1)) # Damn that would be return n but na i don't want to write that!
def validate(testcases: list[int]) -> None:
    for n in testcases:
        solve = Solution()
        result = solve.gcdOfOddEvenSums(n)
        expected = n   # proven simplification
        if result == expected:
            print(f"Testcase n={n}: Passed (Result={result})")
        else:
            print(f"Testcase n={n}: Failed (Result={result}, Expected={expected})")
validate([1,2,3,4,5,6,7,7,8])