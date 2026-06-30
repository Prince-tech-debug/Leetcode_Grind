class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m = len(words), len(words[0])
        total_len = n * m
        word_set = {}
        for i in words:
            word_set[i] = word_set.get(i, 0) + 1
        idx = []
        
        left, right = 0, total_len - 1

        while right < len(s):
            seen = {}
            is_correct = True   #

            for i in range(left, right+1, m):
                word = s[i:i+m]
                if word in word_set and seen.get(word, 0)< word_set[word]:
                    seen[word] = seen.get(word, 0) + 1
                else:
                    is_correct = False
                    break

            if is_correct and seen == word_set:
                idx.append(left)

            left += 1
            right += 1

        return idx

def validate():
    sol = Solution()

    
    tests = [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
        ("barfoofoobarthefoobarman", ["bar","foo","the"], [6, 9, 12]),
        ("foobarfoobar", ["foo","bar"], [0, 3, 6]),
        ("aaaaaa", ["aa","aa","aa"], [0]),
    ]

    all_passed = True
    for i, (s, words, expected) in enumerate(tests, 1):
        result = sol.findSubstring(s, words)
        if sorted(result) == sorted(expected):
            print(f"Test {i}: PASSED (got {result})")
        else:
            print(f"Test {i}: FAILED (got {result}, expected {expected})")
            all_passed = False

    return all_passed

# Did this because it's a hard Problem :`)
validate()