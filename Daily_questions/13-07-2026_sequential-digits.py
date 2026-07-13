class Solution:
    def __init__(self,s = "123456789"):
        self.listy = []
        for i in range(2,10):
            l, r = 0, i
            while r < 10:
                self.listy.append(int(s[l:r]))
                l+=1
                r+=1
        

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # optimal we can use sliding window for optimallity simulation
        # but the calculation over head will create a tc discripency so we can use precomputed dp of all possible ways
        # listy = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]
        result = []
        for i in self.listy:
            if i >= low and i <= high:
                result.append(i)
        return result
        # well you can use the above constructor to solve this question but i think their exist more elegent way



        #brutish way to do this
        # def is_seq(nums):
        #     listy = []
        #     while nums > 0:
        #         if listy and listy[-1]-1 == nums%10:
        #             listy.append(nums%10)
        #             nums //= 10
        #         elif not listy:
        #             listy.append(nums%10)
        #             nums //= 10
        #         else:
        #             return False
        #     return True
        # result = []
        # for i in range(low,high+1):
        #     if is_seq(i):
        #         result.append(i)
        # return result
            
def validate():
    solve = Solution()
    test = [(100,300, [123,234]),
            (1000, 13000, [1234,2345,3456,4567,5678,6789,12345]),
            (10, 100000000000, solve.listy)]
    for i,j,out in test:
        if solve.sequentialDigits(i,j) == out:
            print("PASSED")
        else:
            print("FAILED")
validate()