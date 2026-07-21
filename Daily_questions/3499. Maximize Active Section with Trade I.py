class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        res = ''
        n = 0          
        prev_z = 0     
        ones = 0       
        mx = 0         
        prev = None    
        
       
        ones = s.count('1')
        
        
        s = s + '1'
        
        for i in s:
            if i == '0':
                n += 1
            else: 
                if prev == '0':
                    
                    if prev_z > 0:
                        mx = max(mx, prev_z + n)
                    prev_z = n
                    n = 0
            prev = i
        
        return ones + mx