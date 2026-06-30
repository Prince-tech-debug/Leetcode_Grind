class Solution:
    def simplifyPath(self, path: str) -> str:
        dirt =  path.split('/')
        result = []
        for i in dirt:
            if i != '' and i != '.':
                if i == "..":
                    if result == []:
                        continue
                    result.pop()
                else:
                    result.append(i)
        
        return '/'+'/'.join(result)
def validate():
    solve = Solution()
    test = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", '/'),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
        ("/a/./b/../../c/", "/c")
    ]
    for input, output in test:
        if solve.simplifyPath(input) == output:
            print(f"Passed  (got {output})")
    return 0

if __name__ == '__main__':
    
    validate()