'''
Problem 28. Implement strStr()
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_str = len(needle)
        cnt = 0
        if(needle or haystack) == '':
            return 0
        for idx in haystack:
            if haystack[cnt:len_str+cnt] == needle:
                return cnt
            cnt+=1
        return -1