class Solution:
	# @param A : list of integers
	# @return an integer
	def cntBits(self, A):
	    mod = 1000000007
	    sum = 0
	    n = len(A)
	    
	    for i in range(64):
	        cnt1 = 0
	        for j in range(n):
	            if A[j]&(1<<i):
	                cnt1 += 1
	        
	        sum = (sum + (cnt1)*(n-cnt1)*2)%mod
	       
	    return sum % mod