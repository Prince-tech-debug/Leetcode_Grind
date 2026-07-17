import bisect
class Solution:
    def gcdValues(self, nums, queries):
        M = max(nums)
        cnt = [0] * (M+1)
        for x in nums:
            cnt[x] += 1

        for d in range(1, M+1):
            for multiple in range(2*d, M+1, d):
                cnt[d] += cnt[multiple]

        exact = [0] * (M+1)
        for d in range(M, 0, -1):
            total = cnt[d] * (cnt[d]-1) // 2
            for multiple in range(2*d, M+1, d):
                total -= exact[multiple]
            exact[d] = total

        gcds = []
        prefix = []
        total = 0
        for g in range(1, M+1):
            if exact[g]:
                gcds.append(g)
                total += exact[g]
                prefix.append(total)

        ans = []
        for q in queries:
            idx = bisect.bisect_left(prefix, q+1)
            ans.append(gcds[idx])
        return ans
# From now on i am not uploading validate so you can direct run it on leet code if you want.