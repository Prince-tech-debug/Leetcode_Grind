class Solution:
    def maxProduct(self, n: int) -> int:
        if n //10 == 0:
            return 0
        res = []
        while n > 0:
            res.append(n % 10)
            n //= 10
        res.sort(reverse = True)
        return res[0] * res[1]
