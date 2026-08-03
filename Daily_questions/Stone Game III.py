class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @lru_cache(None)
        def recur(i):
            if i >= n:
                return  0
            best, total = float('-inf'),0
            for j in range(i, min(n, i + 3)):
                total += stoneValue[j]
                best = max(best, total - recur(j + 1))
            return best
        score_diff = recur(0)
        if score_diff > 0:
            return "Alice"
        elif score_diff < 0:
            return "Bob"
        else:
            return "Tie"
        





        #This won't work because of negetives
        # prefix_sum = [0]
        # for i in stoneValue:
        #     prefix_sum.append(i + prefix_sum[-1])
        # total = prefix_sum[-1]
        # memo = {}
        # def recur(i,s):
        #     if (i,s) in memo:
        #         return memo[(i,s)]
        #     if i >= len(stoneValue):
        #         return 0
        #     take = float('-inf') if s == 0 else float('inf')
        #     if s == 0:
        #         for j in range(i+1, min(i + 4, len(stoneValue))):
        #             take = max(take, prefix_sum[j] - prefix_sum[i] + recur(j, 1))
        #     if s== 1:
        #         for j in range(i+1, min(i + 4, len(stoneValue))):
        #             take = min(take, recur(j, 0))
        #     memo[(i,s)] = take if take != float('inf') and take != float('-inf') else 0
        #     return memo[(i,s)]
        # n = recur(0,0)
        # if n > total - n:
        #     return 'Alice'
        # elif n < total - n:
        #     return "Bob"
        # else:
        #     return 'Tie'