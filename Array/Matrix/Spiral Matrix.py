class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n, m = len(matrix), len(matrix[0])
        result = []
        def one_cycle(co,ordi, n, m,result):
            if m-2*co != 1 and n-2*ordi != 1:

                for i in range(co,m-1-co):
                    result.append(matrix[co][i])
                for i in range(ordi,n-1-ordi):
                    result.append(matrix[i][m-1-co])
                for i in range(m-1-co, co, -1):
                    result.append(matrix[n-1-ordi][i])
                for i in range(n-1-ordi, ordi, -1):
                    result.append(matrix[i][ordi])
            if m-2*co == 1 and n-2*ordi != 1:
                for i in range(ordi, n - ordi):
                    result.append(matrix[i][ordi])
            if n-2*ordi == 1 and m-2*co != 1:
                for i in range(co, m- co):
                    result.append(matrix[co][i])
            if n-2*ordi == 1 and m-2*co == 1:
                result.append(matrix[co][ordi])
        def recur(i,j,n,m,result):
            if n - 2*j <= 0 or m - 2*i <= 0:
                return 
            else:
                one_cycle(i,j,n,m,result)
                i += 1
                j += 1
            recur(i,j,n,m,result)
        recur(0,0, n, m, result)


        return result
def validation():
    solve = Solution()
    test = [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])
            ]
    for input,output in test:
        if solve.spiralOrder(input) == output:
            print(f"PASSED :) (got {output})")
        else:
            print(f"FAILED :( (got {output})")
    return 0
if __name__ == '__main__':
    validation()