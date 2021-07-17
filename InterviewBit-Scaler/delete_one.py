class Solution:
    # @param A : list of integers
    # @return an integer
    
    def gcd(self, a,b):
        if b==0:
            return a
        return self.gcd(b, a%b)
        
    def solve(self, A):
        tmp_ar=list()
        ret_ar=list()
        for i in range(0, len(A)):
            if len(tmp_ar) == 0:
                tmp_ar.append(A[i])
                A.remove(A[i])
                ret_ar.append(self.gcd(A[0],A[1]))
            else:
                tmp_ar.append(A[i-1])
                A[i-1] = tmp_ar[i-1]
                ret_ar.append(self.gcd(A[0],A[1]))
        return max(ret_ar)
        
