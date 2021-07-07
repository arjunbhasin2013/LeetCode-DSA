'''
Problem Description

Given an integer A, return the number of trailing zeroes in A! i.e. factorial of A.

Note: Your solution should run in logarithmic time complexity.
'''

class Solution:
	# @param A : integer
	# @return an integer
        
    def trailingZeroes(self, A):
        count = 0
        i = 5

        while (A//i != 0):
            count+=1
            i = i*5
        return count
            
