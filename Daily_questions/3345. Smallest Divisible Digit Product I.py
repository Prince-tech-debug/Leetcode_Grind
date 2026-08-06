class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 20):
            node = i
            pro = 1
            while node != 0:
                pro *= node % 10
                node //= 10
            if pro %t == 0:
                return i
        return -1
