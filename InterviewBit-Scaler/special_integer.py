class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lo, hi = 1, len(A)
        n = len(A)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            s = sum(A[:mid])
            if s > B:
                hi = mid - 1
                continue
            for i in range(mid, n):
                s += A[i] - A[i - mid]
                if s > B:
                    hi = mid - 1
                    break
            else:
                lo = mid + 1
                ans = mid
        return ans