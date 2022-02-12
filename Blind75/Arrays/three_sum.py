#https://leetcode.com/problems/3sum/

arr = [-3,3,1,2,5]
target = 0

def three_sum(arr, target):
    arr.sort()
    
    #print(arr)
    for idx, val in enumerate(arr):
        if idx > 0 and arr[idx-1] == arr[idx]:
            continue 
        else:
            left, right = 0, len(arr)-1
            
            while left<right:
                three_sum = val + arrleft] + arr[right]
                if three_sum > target:
                    right-=1
                elif three_sum < target:
                    left+=1
                else:
                    return [val, arr[left], arr[right]]
    
print(three_sum(arr, target))