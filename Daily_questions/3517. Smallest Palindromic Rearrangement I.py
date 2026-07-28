class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 3 or len(s) == 1:
            return s
        s = Counter(s)
        mx = max(s)
        mn = min(s)
        print(mn)
        print(mx)
        counting = {}
        res = []
        last = ''
        for i in range(ord(mn),ord(mx)+1):
            char = chr(i)
            if char in s and s[char] % 2 == 0:
                k = s[char]//2
                for i in range(k):
                    res.append(char)
                s[char] = 0
            elif char in s and s[char] % 2 == 1 and s[char] >= 1:
                k = s[char]//2
                for i in range(k):
                    res.append(char)
                last = char
            
        print(res)
        print(last)
        res = res + [last] + res[::-1]
        return ''.join(res)
        
        # if len(s) % 2 = 1
