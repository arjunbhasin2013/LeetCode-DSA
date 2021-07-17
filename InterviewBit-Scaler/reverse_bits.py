class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        i = 31
        ret = 0
        while i >= 0:
            temp = ((A & 1<<i) >> i)&1
            ret = ret | temp << (31-i)
            i -= 1
        return ret