'''
Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        return self.find_peak(A, 0, n-1, n)
        

    def find_peak(self,arr, low, high, n):
        mid = low + (high-low)/2
        mid = int(mid)
        
        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            return arr[mid]
            
        elif (mid > 0 and arr[mid - 1] > arr[mid]):
            return self.find_peak(arr, low, (mid - 1), n)

        else:
            return self.find_peak(arr, (mid + 1), high, n)
            
