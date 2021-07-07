'''
Problem Description

Given an array of integers A, every element appears twice except for one. Find that single one.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        v=0
        for i in range(len(A)):
            v^=A[i]
        return v