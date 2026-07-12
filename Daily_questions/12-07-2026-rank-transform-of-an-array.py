class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        hash_map = {}
        nums = sorted(arr)
        hash_map[nums[0]] = 1
        rank = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                rank += 1
                hash_map[nums[i]] = rank
        for i in range(len(arr)):
            arr[i] = hash_map[arr[i]]
        return arr

def validate():
    try:
        solve = Solution()
        tests = [([40,10,20,30],[4,1,2,3]),
                ([100,100,100],[1,1,1]),
                ([37,12,28,9,100,56,80,5,12], [5,3,4,2,8,6,7,1,3])]
        for i,j in tests:
            if solve.arrayRankTransform(i) == j:
                print(f"Passed the output is:-> {j}")
            else:
                print(f"Failed the output is:-> {solve.arrayRankTransform(i)} \nThe expected was:-> {j}")
    except:
        print("Their is an error in the code.")
validate()