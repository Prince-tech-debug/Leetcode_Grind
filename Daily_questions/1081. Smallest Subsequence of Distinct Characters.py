class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = [s[0]]
        seen = {s[0]}
        for ch in s:
            freq[ch] -= 1
            if ch not in seen :

                while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                    n = stack.pop()
                    seen.remove(n)
                stack.append(ch)
                seen.add(ch)
        return  ''.join(stack)
