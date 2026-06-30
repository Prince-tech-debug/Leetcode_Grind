class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        hash_map = {'a': 0, 'b': 0, 'c': 0}
        left, res = 0, 0

        for right in range(n):
            hash_map[s[right]] += 1
            while hash_map['a'] > 0 and hash_map['b'] > 0 and hash_map['c'] > 0:
                res += n - right   # all substrings starting at left and ending at >= right are valid
                hash_map[s[left]] -= 1
                left += 1

        print(f'Total number of string present which have all three characters are: {res}') 

solve = Solution()
s = 'abcabc' # Expected output is 10
solve.numberOfSubstrings(s)


