'''
implementing binary search iteratively
'''

def binary_search(data, target, low, high):
    while high>=low:
        mid = (low+high)//2
        if target == data[mid]:
            return 1
        else:
            if data[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return -1

if __name__ == "__main__":
    data = [1,2,3,4,5,6]
    print(binary_search(data, 7, 0, len(data)))


