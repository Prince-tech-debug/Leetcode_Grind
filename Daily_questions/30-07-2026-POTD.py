class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)//8
        mod = len(word)% 8
        result = 0
        j = 0
        for i in range(n):
            j = i + 1
            result += 8 * (i  + 1)
        print(j)
        result += mod * (j + 1)
        return result