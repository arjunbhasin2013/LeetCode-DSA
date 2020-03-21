'''

Problem 387. First Unique Character in a String

'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_char_store = {}
        list_s = []

        for idx in s:
            if idx in dict_char_store:
                dict_char_store[idx]+=1
                if idx in list_s:
                    list_s.remove(idx)
            else:
                dict_char_store[idx] = 1
                list_s += idx
                
        if len(list_s) == 0:
            return -1
        else:
            return s.index(list_s[0])


'''

104 / 104 test cases passed.
Status: Accepted
Runtime: 124 ms
Memory Usage: 13 MB

'''