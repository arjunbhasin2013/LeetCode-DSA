'''
implementing binary search using recursion
'''

def binary_search(data, target, low, high):
    mid = (low+high)//2

    if data[mid] == target:
        return 1

    else:
        if data[mid]>target:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7]
    target = 4
    print(binary_search(data, target, 0, len(data)))


