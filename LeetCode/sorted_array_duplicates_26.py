'''

Problem 26. Remove duplicates from Sorted Array

'''

def remove_duplicates(nums):
    non_duplicates = list()

    for idx in range(0, len(nums)):
        if idx == len(nums)-1 and nums[idx] not in non_duplicates:
            non_duplicates.append(nums[idx])
        else: 
            if nums[idx] != nums[idx+1] and nums[idx+1] not in non_duplicates:
                non_duplicates.append(nums[idx])

    return len(non_duplicates)

test = [0,0,1,1,1,2,2,3,3,4,4,4,4,4,4,4,4,4,5]
print(remove_duplicates(test))