#https://leetcode.com/problems/two-sum/

arr = [1,3,4,5,7,11]
target = 7

def two_sum(arr, target):
    start_ptr = 0 
    end_ptr = len(arr) -1 
    
    while start_ptr<end_ptr:
        curr_sum = arr[start_ptr] + arr[end_ptr]
        if curr_sum > target:
            end_ptr-=1
        elif curr_sum < target:
            start_ptr+=1
        else:
            return [1+start_ptr,1+end_ptr]
     
print(two_sum(arr, target))
        
            