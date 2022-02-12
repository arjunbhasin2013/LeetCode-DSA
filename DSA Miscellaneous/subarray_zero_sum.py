'''
Code limit is 10^5 - quadratic solution cannot work

Quadratic solution 
'''

def subarray_sum_quadratic(arr):
    for i in range(0, len(arr)):
        sum_calc = 0
        for j in range(i, len(arr)):
            sum_calc+=arr[j]
            if sum_calc == 0:
                return True
    return False

def optimal_solution(arr): #using set
    used_set = set()
    sum_calc=0

    for i in range(0, len(arr)):
        used_set.add(sum_calc)
        sum_calc+=arr[i]

        if sum_calc in used_set:
            return True
    return False

if __name__ == "__main__":
<<<<<<< HEAD
    arr = [2,30,-2]
=======
    arr = [2,1,3,-4,-2]
>>>>>>> a640dbb916efe6db2be59c953c406b14b81f8430
    print(optimal_solution(arr))