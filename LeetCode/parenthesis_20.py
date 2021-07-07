'''
Problem 20. Valid Parentheses
'''

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        left = '{(['
        right = '})]'
        stack = deque()
        
        if len(s)%2!=0:return False
        if s=='':return False

        for i in s:
            if i in left:
                stack.append(i)
            elif i in right:
                if len(stack)==0:
                    return False
                elif right.index(i) != left.index(stack.pop()):
                    return False
        if len(stack)==0:
            return True

s = Solution()
print(s.isValid('{()}'))

'''

Runtime: 24 ms, faster than 95.46% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.1 MB, less than 86.20% of Python3 online submissions for Valid Parentheses.

'''