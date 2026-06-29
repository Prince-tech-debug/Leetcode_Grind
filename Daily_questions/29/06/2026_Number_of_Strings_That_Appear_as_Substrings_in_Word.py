
class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count

word = "abc"
patterns = ["a","abc","bc","d"] # Expected output : 3
solve = Solution()
print(solve.numOfStrings(patterns, word))