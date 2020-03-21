'''

Problem 58. Length of Last Word

'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
    
        if len(s) == 0:
            return 0

        elif len(s) != 0:
            last_word = s.split(' ')[-1]
            if last_word == '':
                last_word = s.split(' ')[-2]
        cnt = 0

        for idx in last_word:
            cnt+=1 
        return cnt


'''

59 / 59 test cases passed.
Status: Accepted
Runtime: 24 ms
Memory Usage: 13 MB

'''