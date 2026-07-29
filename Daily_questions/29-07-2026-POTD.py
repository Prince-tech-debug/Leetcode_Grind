INF = 10**6 + 1
N = 24

# Precompute Pascal's triangle
C = [[0] * N for _ in range(N)]
def Pascal():
    if C[0][0] == 1:  # already computed
        return
    C[0][0] = 1
    for i in range(1, N):
        C[i][0] = C[i][i] = 1
        for j in range(1, i // 2 + 1):
            C[i][j] = C[i][i - j] = C[i - 1][j - 1] + C[i - 1][j]

def comb(n: int, k: int) -> int:
    if n < N:
        return C[n][k]
    if 2 * k > n:
        k = n - k
    ans = 1
    for i in range(1, k + 1):
        ans = ans * (n - i + 1) // i
        if ans >= INF:
            return INF
    return ans

def perm(freq: List[int], sz: int) -> int:
    ans = 1
    for f in freq:
        if f == 0:
            continue
        ans *= comb(sz, f)
        if ans >= INF:
            return INF
        sz -= f
    return ans

class Solution:
    @staticmethod
    def smallestPalindrome(s: str, k: int) -> str:
        Pascal()
        n = len(s)
        n0 = n // 2
        freq = [0] * 26
        for i in range(n0):
            freq[ord(s[i]) - ord('a')] += 1

        total = perm(freq, n0)
        if k > total:
            return ""

        left = []
        sz = n0
        for i in range(n0):
            for c in range(26):
                if freq[c] == 0:
                    continue
                freq[c] -= 1
                sz -= 1
                cnt = perm(freq, sz)
                if cnt >= k:
                    left.append(chr(ord('a') + c))
                    break
                else:
                    k -= cnt
                    freq[c] += 1
                    sz += 1

        right = left[::-1]
        if n % 2 == 1:
            left.append(s[n // 2])
        return "".join(left + right)