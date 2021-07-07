'''
Problem Description

Given an integer array A of size N.
Find the minimum number of elements that need to be removed such that the GCD of the resulting array becomes 1.

If not possible then return -1.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        while B:
            A, B = B, A % B
        return  A
    
    def solve(self, A):
        arr_gcd = A[0]
        for ele in A[1:]:
            arr_gcd = self.gcd(arr_gcd, ele)
            if arr_gcd == 1:
                return 0
        return -1
