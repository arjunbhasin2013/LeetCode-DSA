'''
49. Given an array of strings, group anagrams together.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_sort = {}
        
        for idx in strs:
            x = "".join(sorted(idx))

            if x in dict_sort:
                dict_sort[x].append(idx)
            else:
                dict_sort[x] = [idx]

        return dict_sort.values()


'''
101 / 101 test cases passed.
Status: Accepted
Runtime: 88 ms
Memory Usage: 16.8 MB

'''