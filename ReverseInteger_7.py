'''

Problem 7. Reverse Integer

'''


class Solution:
    def rev(self,num):
        num = int(str(num)[::-1])
        
        LIMIT_VAL = 2**31 
        
        if (LIMIT_VAL-1) > num > -(LIMIT_VAL):
            return num
        
        return 0
    
    def reverse(self,x: int) -> int:
        if x<0:
            x*=-1
            rev_out = self.rev(x)
            return int('-'+str(rev_out))
        else:
            return self.rev(x)
        `


'''

1032 / 1032 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 13 MB

'''