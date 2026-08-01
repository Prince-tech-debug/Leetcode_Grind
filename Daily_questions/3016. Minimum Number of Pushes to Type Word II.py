class Solution:
    def minimumPushes(self, word: str) -> int:
        res, lev, levels = [j for i,j in Counter(word).items()], [], []
        res.sort(reverse = True)

        for i in res:
            lev.append(i)
            if len(lev) % 8 == 0:
                levels.append(lev)
                lev = []
        levels.append(lev)

        res = 0
        for i,j in enumerate(levels):
            res += (sum(j) * (i+1))
        print(levels)
        return res

