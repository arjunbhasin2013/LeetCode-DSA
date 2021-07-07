'''

Problem 9. Palindrome Number

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp_str = str(x)[::-1]
        
        if str(x) == tmp_str:
            return True
        return False


'''

11509 / 11509 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 12.8 MB

'''