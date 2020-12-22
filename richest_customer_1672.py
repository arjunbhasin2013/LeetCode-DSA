'''
1672. Richest Customer Wealth
'''

def maximum_wealth(list_object):
    highest = 0

    for i in range(0, len(list_object)):
        cnt=0
        for j in range(0, len(list_object[i])):
            cnt+=list_object[i][j]
            if cnt>highest:
                highest=cnt
    print(highest)

maximum_wealth([[1,2,3],[4,5,6]])


'''
295 / 295 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 14 MB

'''