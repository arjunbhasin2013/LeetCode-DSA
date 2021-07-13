'''
A lucky number is a number which has exactly 2 distinct prime divisors.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        sieve = [0 for i in range(n)]

        for i in range(2, n):
            if sieve[i-1]==0:
                cnt=0
                sieve[i-1]=cnt+1
                for j in range(i+i, n+1, i):
                    sieve[j-1]+=1

        cnt=0
        for i in range(1, n+1):
            if sieve[i-1] == 2:
                cnt+=1
        return cnt