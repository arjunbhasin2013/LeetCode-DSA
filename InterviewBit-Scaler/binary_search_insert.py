'''
Binary search insert element
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        return self.binary_search(A,B,0, len(A)-1)
        
    def binary_search(self,arr, target, low, high):
        while high>=low:
            mid = (high+low)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid-1

            else:
                low = mid+1
        return high+1

s = Solution()
A = [1]
B = 1
print(s.searchInsert(A,B))
