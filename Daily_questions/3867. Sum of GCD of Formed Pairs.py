class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        new = []
        mx = float('-inf')
        for num in nums:
            mx = max(mx, num)
            new.append(gcd(num,mx))
        print(new)
        new.sort()
        i, j = 0, len(new)-1
        result = 0
        while i<j:
            result += gcd(new[i], new[j])
            i+=1
            j-=1
        return result